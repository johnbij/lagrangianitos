import tempfile
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

import logros


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


class TestE2EUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmpdir = tempfile.TemporaryDirectory()
        cls._ranking_original = logros.RANKING_FILE
        logros.RANKING_FILE = str(Path(cls._tmpdir.name) / "ranking.json")

    @classmethod
    def tearDownClass(cls):
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


if __name__ == "__main__":
    unittest.main()
