import socket
import sys
import requests

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP Address for {domain}: {ip_address}")
        return ip_address
    except socket.gaierror:
        print(f"Couldn't resolve the host {domain}")
        return None

def scan_ports(ip_address, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")
        sock.close()
    return open_ports

def test_directories(url, directories):
    for directory in directories:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Directory {directory} is available at {full_url}")

if __name__ == "__main__":
    target_domain = input("Enter the target domain: ")
    target_ip = get_ip_address(target_domain)

    if target_ip:
        target_ports = [21, 22, 80, 443, 8080]  # You can modify the list of ports as needed
        open_ports = scan_ports(target_ip, target_ports)

        if open_ports:
            print("Testing directories:")
            target_url = f"http://{target_domain}"

            directories_to_test = ["index", "images", "download", "2006", "news", "crack", "serial", "warez", "full",
                                   "12", "contact", "about", "search", "spacer", "privacy", "11", "logo", "blog",
                                   "new", "10", "cgi-bin", "faq", "rss", "home", "img", "default", "2005", "products",
                                   "sitemap", "archives", "1", "09", "links", "01", "08", "06", "2", "07", "login",
                                   "articles", "support", "05", "keygen", "article", "04", "03", "help", "events",
                                   "archive", "admin.php", "register", "en", "forum", "software", "downloads", "3", "security",
                                   "13", "category", "4", "content", "14", "main", "15", "press", "media", "templates",
                                   "services", "icons", "resources", "info", "profile", "16", "2004", "18", "docs",
                                   "contactus", "html", "features", "files", "20", "21", "5", "22", "page", "6", "misc",
                                   "19", "partners", "24", "terms", "2007", "23", "i", "17", "27", "26", "top", "9",
                                   "legal", "30", "banners", "xml", "29", "28", "7", "tools", "projects", "25", "0",
                                   "user", "feed", "themes", "linux", "forums", "jobs", "business", "8", "video", "email",
                                   "books", "banner", "reviews", "view", "graphics", "research", "feedback", "print",
                                   "pdf", "ads", "modules", "2003", "company", "blank", "pub", "games", "copyright",
                                   "common", "site", "comments", "people", "aboutus", "product", "sports", "logos",
                                   "buttons", "english", "story", "image", "uploads", "31", "subscribe", "blogs", "gallery",
                                   "atom", "newsletter", "stats", "music", "careers", "pages", "publications", "technology",
                                   "calendar", "stories", "photos", "papers", "community", "data", "history", "arrow",
                                   "submit", "www", "s", "web", "library", "wiki", "header", "education", "go", "internet",
                                   "in", "b", "advertise", "a", "spam", "nav", "mail", "users", "Images", "topics",
                                   "members", "disclaimer", "store", "clear", "feeds", "c", "awards", "2002", "Default",
                                   "general", "pics", "dir", "signup", "solutions", "map", "News", "public", "doc", "de",
                                   "weblog", "index2", "shop", "contacts", "homepage", "fr", "button", "travel", "list",
                                   "pixel", "viewtopic", "documents", "overview", "tips", "adclick", "contact_us", "movies",
                                   "wp-content", "catalog", "us", "p", "staff", "hardware", "wireless", "global", "screenshots",
                                   "apps", "online", "version", "directory", "mobile", "other", "advertising", "tech",
                                   "welcome", "admin", "t", "policy", "faqs", "2001", "link", "training", "releases", "space",
                                   "member", "static", "join", "health", "weather", "reports", "scripts", "browse", "windows",
                                   "showallsites", "programs", "FireFox_Reco", "EWbutton_Community", "EWbutton_GuestBook", "menu"]

            test_directories(target_url, directories_to_test)
        else:
            print("No open ports found.")
