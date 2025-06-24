import os
import json
from colorama import init, Fore, Style
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from time import sleep

# Initialize
init(autoreset=True)
console = Console()

# === Display animated header ===
def show_banner():
    console.print(Panel.fit(
        "[bold cyan]📧 Email Country Filter by Martin Versa[/bold cyan]\n"
        "[green]🔍 Classify emails by domain & country[/green]\n"
        "[yellow]🧠 Powered by Python + Colorama + Rich[/yellow]\n"
        "[white]Contact: [link=https://t.me/martinversa]@martinversa[/link][/white]",
        title="Martin Versa CLI Tool", border_style="bold magenta"
    ))

# === Create output folder ===
def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        console.print(f"[bold red]✗ Failed to create directory {directory}: {e}[/bold red]")
        raise

# === Load config ===
def load_domain_config(config_path='domain_config.json'):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[yellow]✗ Domain config file not found. Using default.[/yellow]")
        return DEFAULT_DOMAIN_CONFIG
    except Exception as e:
        console.print(f"[red]✗ Failed to load config: {e}[/red]")
        raise

# === Default domain map ===
DEFAULT_DOMAIN_CONFIG = {
    "us": {  # Amerika Serikat
        "domains": [
            "gmail.com", "yahoo.com", "aol.com", "hotmail.com",
            "outlook.com", "live.com", "icloud.com", "msn.com",
            "comcast.net", "verizon.net", "att.net", "bellsouth.net",
            "cox.net", "sbcglobal.net", "earthlink.net", "charter.net",
            "mail.com", "gmx.com", "protonmail.com", "fastmail.com",
            "ymail.com", "rocketmail.com"
        ]
    },
    "br": {  # Brasil
        "domains": [
            "gmail.com.br", "yahoo.com.br", "hotmail.com.br",
            "uol.com.br", "bol.com.br", "terra.com.br", "zipmail.com.br",
            "ig.com.br", "r7.com", "globo.com"
        ]
    },
    "in": { "domains": [ "gmail.co.in", "yahoo.in", "yahoo.co.in", "rediffmail.com", "in.com", "hotmail.co.in", "outlook.in", "live.in", "indiatimes.com" ] },
    "de": { "domains": [ "gmail.de", "yahoo.de", "hotmail.de", "gmx.de", "web.de", "t-online.de", "outlook.de", "mail.de", "freenet.de", "posteo.de" ] },
    "fr": { "domains": [ "gmail.fr", "yahoo.fr", "hotmail.fr", "outlook.fr", "laposte.net", "orange.fr", "sfr.fr", "free.fr", "wanadoo.fr", "bouyguestelecom.fr" ] },
    "uk": { "domains": [ "gmail.co.uk", "yahoo.co.uk", "hotmail.co.uk", "outlook.co.uk", "btinternet.com", "virginmedia.com", "blueyonder.co.uk", "sky.com", "talktalk.net", "ntlworld.com", "mail.com" ] },
    "ru": { "domains": [ "mail.ru", "yandex.ru", "rambler.ru", "gmail.ru", "hotmail.ru", "outlook.ru", "bk.ru", "list.ru", "inbox.ru" ] },
    "cn": { "domains": [ "qq.com", "163.com", "126.com", "sina.com", "yeah.net", "aliyun.com", "foxmail.com", "tom.com" ] },
    "kr": { "domains": [ "naver.com", "hanmail.net", "daum.net", "nate.com", "kakao.com", "empas.com", "yahoo.co.kr" ] },
    "jp": { "domains": [ "yahoo.co.jp", "gmail.com", "hotmail.co.jp", "outlook.jp", "docomo.ne.jp", "au.com", "ezweb.ne.jp", "softbank.ne.jp" ] },
    "mx": { "domains": [ "gmail.com.mx", "yahoo.com.mx", "hotmail.com.mx", "prodigy.net.mx", "live.com.mx", "outlook.com.mx" ] },
    "ca": { "domains": [ "gmail.ca", "yahoo.ca", "hotmail.ca", "outlook.ca", "sympatico.ca", "rogers.com", "telus.net", "shaw.ca" ] },
    "au": { "domains": [ "gmail.com.au", "yahoo.com.au", "hotmail.com.au", "outlook.com.au", "bigpond.com", "optusnet.com.au", "internode.on.net" ] },
    "es": { "domains": [ "gmail.es", "yahoo.es", "hotmail.es", "outlook.es", "terra.es", "telefonica.net", "ono.com" ] },
    "it": { "domains": [ "gmail.it", "yahoo.it", "hotmail.it", "outlook.it", "libero.it", "virgilio.it", "tiscali.it", "tin.it", "alice.it" ] },
    "ar": { "domains": [ "gmail.com.ar", "yahoo.com.ar", "hotmail.com.ar", "outlook.com.ar", "fibertel.com.ar", "ciudad.com.ar" ] },
    "sa": { "domains": [ "gmail.com.sa", "yahoo.com.sa", "hotmail.com.sa", "outlook.com.sa", "stc.com.sa", "mobily.com.sa" ] }
}

# === Filter emails ===
def filter_and_save_emails_by_country(file_path, output_directory):
    console.print("\n[bold cyan]🔧 Starting email filtering process...[/bold cyan]")
    create_directory(output_directory)
    popular_domains = load_domain_config()

    try:
        for encoding in ['utf-8', 'ISO-8859-1', 'latin-1']:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    emails = [line.strip() for line in file if '@' in line]
                console.print(f"[green]✓ Loaded '{file_path}' successfully with {encoding}[/green]")
                break
            except UnicodeDecodeError:
                continue
        else:
            raise UnicodeDecodeError("Unsupported file encoding.")
    except Exception as e:
        console.print(f"[bold red]✗ Error reading file: {e}[/bold red]")
        return

    email_dict = {}
    other_emails = set()

    with Progress() as progress:
        task = progress.add_task("[cyan]Processing emails...", total=len(emails))
        for email in emails:
            try:
                _, domain_part = email.rsplit('@', 1)
                domain = domain_part.lower()
                found = False

                for country, data in popular_domains.items():
                    if domain in map(str.lower, data["domains"]):
                        email_dict.setdefault(country, {}).setdefault(domain, set()).add(email)
                        found = True
                        break

                if not found:
                    other_emails.add(email)
            except Exception as e:
                console.print(f"[yellow]✗ Error with email {email}: {e}[/yellow]")
            finally:
                progress.update(task, advance=1)
                sleep(0.001)  # Small delay for animation

    # === Write grouped emails ===
    for country, domains in email_dict.items():
        country_folder = os.path.join(output_directory, country)
        create_directory(country_folder)
        for domain, email_set in domains.items():
            output_file = os.path.join(country_folder, f"{domain}.txt")
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write("\n".join(sorted(email_set)))
                console.print(f"[green]✓ {len(email_set)} emails → {country}/{domain}.txt[/green]")
            except IOError as e:
                console.print(f"[red]✗ Failed writing {output_file}: {e}[/red]")

    if other_emails:
        other_output = os.path.join(output_directory, 'other_mail.txt')
        try:
            with open(other_output, 'w', encoding='utf-8') as f:
                f.write("\n".join(sorted(other_emails)))
            console.print(f"[yellow]✓ {len(other_emails)} emails saved to other_mail.txt[/yellow]")
        except IOError as e:
            console.print(f"[red]✗ Failed writing other_mail.txt: {e}[/red]")

    console.print("\n[bold green]✔ Process completed! Check the result folder.[/bold green]")

# === Setup default config ===
CONFIG_FILE = 'domain_config.json'
if not os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_DOMAIN_CONFIG, f, indent=2)
        console.print(f"[green]✓ Created default config: {CONFIG_FILE}[/green]")
    except Exception as e:
        console.print(f"[red]✗ Could not create config file: {e}[/red]")

# === Main ===
if __name__ == "__main__":
    show_banner()
    path = input(Fore.CYAN + "📄 Enter email list file path: ").strip()
    output_dir = "result"
    filter_and_save_emails_by_country(path, output_dir)
