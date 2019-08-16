import pdfkit
from jinja2 import Environment, FileSystemLoader
import time


fecha=time.strftime("%d/%m/%y")

env= Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")

student ={
	'name' : 'Pepito Medina',
	'course' : 'INGLES AasdVANZADO',
	'hours' : 10,
	'date' : fecha

}

html = template.render(student)
f =open('nuevo.html','w')
f.write(html)
f.close

#pdfkit.from_file('nuevo.html','nuevo_pdf.pdf')

options = {
    'page-size': 'Letter',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
}
    

pdfkit.from_string('Hello!', 'out.pdf')

