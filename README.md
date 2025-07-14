# Newy

A small Django project to test deployment.

### Stack
- **Django** — Python web framework  
- **Tailwind CSS** — utility-first styling  
- **Mailgun** — email sending  
- **Railway** — hosting & deployment  

### Setup

```bash
git clone https://github.com/yourusername/newy.git
cd newy
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
