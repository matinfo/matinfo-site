"""Views for Zinnia archive list"""
from django.views.generic.simple import direct_to_template
from django.views.generic import View
from project.utils.xhtml2pdf import PDFTemplateResponseMixin
from zinnia.models import Entry


def get_archive_list(*ka, **kw):
    """Wrapper around the direct to template generic view to
    force the update of the extra context"""
    kw['extra_context'] = {'archives': Entry.published.all()}

    return direct_to_template(*ka, **kw)



def get_resume(PDFTemplateResponseMixin, View):
    template_name = 'staticpages/resume.html'
    pdf_filename = 'resume_Mathieu_Meylan.pdf'

    return direct_to_template(PDFTemplateResponseMixin)
