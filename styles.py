# styles.py
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt


def add_styles(document):
    styles = document.styles

    title_style = styles.add_style("title", WD_STYLE_TYPE.PARAGRAPH)
    title_style.font.size = Pt(14)
    title_style.font.name = "Times New Roman"
    title_style.font.bold = True
    title_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    para_center_style = styles.add_style("para_center", WD_STYLE_TYPE.PARAGRAPH)
    para_center_style.font.size = Pt(11)
    para_center_style.font.name = "Times New Roman"
    para_center_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    table_style = styles.add_style("table", WD_STYLE_TYPE.TABLE)
    table_style.font.size = Pt(11)
    table_style.font.name = "Times New Roman"