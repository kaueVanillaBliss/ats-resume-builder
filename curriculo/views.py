from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Curriculo
from .forms import (
    CurriculoForm, ExperienciaFormSet, FormacaoFormSet, 
    HabilidadeFormSet, IdiomaFormSet, CertificadoFormSet
)

def criar_curriculo(request):
    if request.method == 'POST':
        print("🚀 CLICOU EM SALVAR - INICIANDO VALIDAÇÃO...") # Debug
        
        form = CurriculoForm(request.POST)
        
        # Prefixos são essenciais para o JavaScript funcionar
        f_exp = ExperienciaFormSet(request.POST, prefix='experiencia')
        f_form = FormacaoFormSet(request.POST, prefix='formacao')
        f_hab = HabilidadeFormSet(request.POST, prefix='habilidade')
        f_idi = IdiomaFormSet(request.POST, prefix='idioma')
        f_cert = CertificadoFormSet(request.POST, prefix='certificado')

        # 1. Valida o Pai
        if form.is_valid():
            curriculo = form.save(commit=False) # Cria na memória mas não salva no banco ainda
            
            # Vincula os filhos ao pai
            f_exp.instance = curriculo
            f_form.instance = curriculo
            f_hab.instance = curriculo
            f_idi.instance = curriculo
            f_cert.instance = curriculo

            # 2. Valida os Filhos
            validos = True
            
            # Checagem individual para mostrar o erro no terminal
            if not f_exp.is_valid():
                print("❌ ERRO NA EXPERIÊNCIA:", f_exp.errors)
                print("   Erros não-form:", f_exp.non_form_errors())
                validos = False
            
            if not f_form.is_valid():
                print("❌ ERRO NA FORMAÇÃO:", f_form.errors)
                validos = False

            if not f_hab.is_valid():
                print("❌ ERRO NA HABILIDADE:", f_hab.errors)
                validos = False
            
            if not f_idi.is_valid():
                print("❌ ERRO NO IDIOMA:", f_idi.errors)
                validos = False
            
            if not f_cert.is_valid():
                print("❌ ERRO NO CERTIFICADO:", f_cert.errors)
                validos = False

            # Se tudo for válido, salva de verdade
            if validos:
                print("✅ TUDO VÁLIDO! SALVANDO NO BANCO...")
                curriculo.save() # Salva o pai
                f_exp.save()
                f_form.save()
                f_hab.save()
                f_idi.save()
                f_cert.save()
                return render(request, 'curriculo/sucesso.html', {'curriculo': curriculo})
            else:
                print("⚠️ SALVAMENTO BLOQUEADO POR ERROS NOS FILHOS (Veja acima)")
        
        else:
            print("❌ ERRO NO FORMULÁRIO PRINCIPAL (DADOS PESSOAIS):", form.errors)

    else:
        # GET (Carregamento da página)
        form = CurriculoForm()
        f_exp = ExperienciaFormSet(prefix='experiencia')
        f_form = FormacaoFormSet(prefix='formacao')
        f_hab = HabilidadeFormSet(prefix='habilidade')
        f_idi = IdiomaFormSet(prefix='idioma')
        f_cert = CertificadoFormSet(prefix='certificado')

    return render(request, 'curriculo/criar.html', {
        'form': form,
        'f_exp': f_exp,
        'f_form': f_form,
        'f_hab': f_hab,
        'f_idi': f_idi,
        'f_cert': f_cert
    })

def gerar_pdf(request, id_curriculo):
    curriculo = get_object_or_404(Curriculo, id=id_curriculo)
    html_string = render_to_string('curriculo/pdf_template.html', {'c': curriculo})
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Curriculo_{curriculo.nome_completo}.pdf"'
    return response