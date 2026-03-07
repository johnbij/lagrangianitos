import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

import logros


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


class TestE2EUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmpdir = tempfile.TemporaryDirectory()
        cls._ranking_original = logros.RANKING_FILE
        logros.RANKING_FILE = str(Path(cls._tmpdir.name) / "ranking.json")

        # Mock auth so tests run without Supabase credentials
        cls._patch_init = patch("auth.auth_ui.init_session")
        cls._patch_logged = patch("auth.auth_ui.is_logged_in", return_value=True)
        cls._patch_sidebar = patch("auth.auth_ui.show_user_sidebar")
        cls._patch_init.start()
        cls._patch_logged.start()
        cls._patch_sidebar.start()

    @classmethod
    def tearDownClass(cls):
        cls._patch_init.stop()
        cls._patch_logged.stop()
        cls._patch_sidebar.stop()
        logros.RANKING_FILE = cls._ranking_original
        cls._tmpdir.cleanup()

    def _run_app(self):
        return AppTest.from_file(str(APP_PATH)).run(timeout=60)

    def test_bienvenida_to_dashboard(self):
        at = self._run_app()
        self.assertEqual(at.radio[0].value, "🐉 Bienvenida")
        self.assertTrue(any("LAGRANGIANITOS" in md.value for md in at.markdown))

        at.button(key="cta_dashboard").click().run(timeout=60)
        self.assertEqual(at.radio[0].value, "🏠 Dashboard PAES")
        self.assertEqual(at.button(key="m_n").label, "🔢 Números")

    def test_audio_upload_page_renders(self):
        at = self._run_app()
        at.radio[0].set_value("🎵 Subir Audio").run(timeout=60)
        self.assertEqual(at.radio[0].value, "🎵 Subir Audio")
        self.assertTrue(any("SUBIR AUDIO" in md.value for md in at.markdown))
        # Header banner should mention accepted audio formats
        self.assertTrue(any("MP3" in md.value for md in at.markdown))

    def test_sidebar_menu_renders_pages(self):
        at = self._run_app()

        at.radio[0].set_value("📂 Biblioteca de PDFs").run(timeout=60)
        self.assertEqual(at.radio[0].value, "📂 Biblioteca de PDFs")
        self.assertEqual(at.button(key="back_pdf").label, "← Volver")
        self.assertTrue(any("BIBLIOTECA DE RECURSOS" in md.value for md in at.markdown))
        self.assertTrue(any("PAES M1 — Verano 2026" in md.value for md in at.markdown))

        at.button(key="back_pdf").click().run(timeout=60)
        at.radio[0].set_value("🏆 Ranking").run(timeout=60)
        self.assertEqual(at.radio[0].value, "🏆 Ranking")
        self.assertEqual(at.text_input(key="input_nick").label, "Tu nick:")
        self.assertEqual(at.button(key="btn_registrar").label, "Unirse 🚀")

    def test_dashboard_class_navigation_and_cronometro(self):
        at = self._run_app()
        at.radio[0].set_value("🏠 Dashboard PAES").run(timeout=60)
        at.button(key="m_n").click().run(timeout=60)

        self.assertEqual(at.button(key="btn_start_crono").label, "▶️ Iniciar")
        at.button(key="btn_start_crono").click().run(timeout=60)
        self.assertEqual(at.button(key="btn_stop_crono").label, "⏹️ Detener")
        at.button(key="btn_stop_crono").click().run(timeout=60)
        self.assertEqual(at.button(key="btn_start_crono").label, "▶️ Iniciar")

        at.button(key="sc_Conjuntos").click().run(timeout=60)
        self.assertEqual(at.button(key="cls_N01").label, "📖 N01: Teoría de Conjuntos")

        at.button(key="cls_N01").click().run(timeout=60)
        self.assertEqual(
            at.button(key="btn_siguiente_top").label,
            "📖 N02: Números Naturales →",
        )
        at.button(key="btn_siguiente_top").click().run(timeout=60)
        self.assertTrue(any("Clase 2 de 7" in md.value for md in at.markdown))

    def test_ranking_registration_flow(self):
        at = self._run_app()
        at.radio[0].set_value("🏆 Ranking").run(timeout=60)

        at.text_input(key="input_nick").set_value("dragon_tester").run(timeout=60)
        at.button(key="btn_registrar").click().run(timeout=60)

        self.assertEqual(at.button(key="btn_cambiar_nick").label, "Cambiar nick")
        self.assertEqual(at.session_state.filtered_state["nick_usuario"], "dragon_tester")

        at.button(key="btn_cambiar_nick").click().run(timeout=60)
        self.assertEqual(at.button(key="btn_registrar").label, "Unirse 🚀")

    def test_pdf_library_loads_all_repo_pdfs(self):
        at = self._run_app()
        at.radio[0].set_value("📂 Biblioteca de PDFs").run(timeout=60)

        expected_count = len(list((Path(__file__).resolve().parents[1] / "pdfs").glob("*.pdf")))
        rendered_count = sum(md.value.count('<div class="pdf-card">') for md in at.markdown)
        self.assertEqual(rendered_count, expected_count)

    def test_pb02_and_pb03_quiz_feedback_is_dynamic(self):
        at = self._run_app()
        at.radio[0].set_value("🏠 Dashboard PAES").run(timeout=60)
        at.button(key="m_d").click().run(timeout=60)
        at.button(key="sc_Probabilidad").click().run(timeout=60)

        at.button(key="cls_PB02").click().run(timeout=60)
        at.radio(key="pb02_quiz_q1").set_value("C").run(timeout=60)
        self.assertTrue(any("✅ ¡Correcta!" in ok.value for ok in at.success))

        at.button(key="btn_siguiente_top").click().run(timeout=60)
        at.radio(key="pb03_quiz_q1").set_value("A").run(timeout=60)
        self.assertTrue(any("❌ Incorrecta." in err.value for err in at.error))

    def test_app_loads_without_streamlit_autorefresh_dependency(self):
        original_import = __import__

        def _import_with_missing_autorefresh(name, *args, **kwargs):
            if name == "streamlit_autorefresh":
                raise ModuleNotFoundError(f"No module named '{name}'")
            return original_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=_import_with_missing_autorefresh):
            at = AppTest.from_file(str(APP_PATH)).run(timeout=60)

        self.assertEqual(at.radio[0].value, "🐉 Bienvenida")


if __name__ == "__main__":
    unittest.main()
