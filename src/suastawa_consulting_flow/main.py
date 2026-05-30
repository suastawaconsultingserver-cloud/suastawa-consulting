import os
import anthropic
from crewai.flow import Flow, listen, start
from pydantic import BaseModel

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


class SuastawaState(BaseModel):
    topic: str = "KJA dan KKP Suastawa Consulting"
    domain: str = "suastawa-consulting.com"
    content: str = ""
    seo: str = ""
    admin_panel: str = ""


class SuastawaFlow(Flow[SuastawaState]):

    @start()
    def prepare(self):
        print(f"Memulai otomasi website: {self.state.topic}")

    @listen(prepare)
    def generate_content(self):
        print("Agent 1: Menulis konten website...")
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"Tulis konten lengkap website {self.state.topic} dalam bahasa Indonesia profesional. Sertakan: hero section, tentang kami, layanan KJA dan KKP, mengapa memilih kami, CTA. Minimum 800 kata format Markdown."}]
        )
        self.state.content = message.content[0].text
        os.makedirs("output", exist_ok=True)
        with open("output/content.md", "w", encoding="utf-8") as f:
            f.write(self.state.content)
        print("✅ Konten selesai!")

    @listen(generate_content)
    def generate_seo(self):
        print("Agent 2: Membuat SEO...")
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": f"Buat paket SEO lengkap untuk {self.state.topic} di domain {self.state.domain}. Sertakan: meta tags HTML, Open Graph tags, JSON-LD schema, 20 keyword target, sitemap XML, robots.txt. Bahasa Indonesia, fokus KJA KKP konsultan pajak akuntan."}]
        )
        self.state.seo = message.content[0].text
        with open("output/seo.md", "w", encoding="utf-8") as f:
            f.write(self.state.seo)
        print("✅ SEO selesai!")

    @listen(generate_seo)
    def generate_admin_panel(self):
        print("Agent 3: Membangun panel admin...")
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            messages=[{"role": "user", "content": f"Buatkan panel admin HTML lengkap untuk {self.state.topic} domain {self.state.domain}. Single file HTML CSS JS inline. Fitur: login JWT, dashboard statistik, CRUD klien, CRUD layanan KJA KKP, upload dokumen, form konten web, pengaturan SEO. Warna tema hijau teal #1D9E75. Fetch API ke https://api.{self.state.domain}. Tulis HANYA kode HTML murni tanpa backtick atau markdown, langsung mulai dari <!DOCTYPE html>"}]
        )
        self.state.admin_panel = message.content[0].text
        html_content = self.state.admin_panel
        if "```html" in html_content:
            html_content = html_content.split("```html")[1].split("```")[0].strip()
        elif "```" in html_content:
            html_content = html_content.split("```")[1].split("```")[0].strip()
        os.makedirs("output/admin", exist_ok=True)
        with open("output/admin/admin.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("✅ Panel admin selesai!")

    @listen(generate_admin_panel)
    def finish(self):
        print("\n=== SEMUA SELESAI ===")
        print("output/content.md       - Konten website")
        print("output/seo.md           - SEO lengkap")
        print("output/admin/admin.html - Panel admin")


def kickoff():
    SuastawaFlow().kickoff()


if __name__ == "__main__":
    kickoff()