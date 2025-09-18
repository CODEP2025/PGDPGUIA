from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Eixo, Procedimento


def home(request):
    q = (request.GET.get("q") or "").strip()
    eixo_id = (request.GET.get("eixo") or "").strip()
    procedimento_id = (request.GET.get("procedimento") or "").strip()
    page_number = request.GET.get("page")

    eixos = Eixo.objects.only("id", "nome").order_by("ordem", "nome")
    qs = Procedimento.objects.select_related("eixo")

    if q:
        qs = qs.filter(
            Q(titulo__icontains=q)
            | Q(o_que_e__icontains=q)
            | Q(quem_tem_direito__icontains=q)
            | Q(documentos_exigidos__icontains=q)
            | Q(procedimentos_passo__icontains=q)
            | Q(base_legal_regimentar__icontains=q)
        )

    if eixo_id:
        qs = qs.filter(eixo_id=eixo_id)

    if procedimento_id:
        qs = qs.filter(id=procedimento_id)

    has_filters = bool(q or eixo_id or procedimento_id)
    if not has_filters:
        qs = qs.none()

    qs = qs.order_by("titulo")

    paginator = Paginator(qs, 15)
    page_obj = paginator.get_page(page_number)

    if eixo_id:
        procedimentos_opcoes = (
            Procedimento.objects.filter(eixo_id=eixo_id)
            .only("id", "titulo")
            .order_by("titulo")
        )
    else:
        procedimentos_opcoes = Procedimento.objects.only("id", "titulo").order_by("titulo")[:300]

    context = {
        "eixos": eixos,
        "procedimentos_opcoes": procedimentos_opcoes,
        "procedimentos": page_obj.object_list,
        "page_obj": page_obj,
    }
    return render(request, "guia/home.html", context)


def procedure_detail(request, slug):
    proc = get_object_or_404(Procedimento.objects.select_related("eixo"), slug=slug)
    return render(request, "guia/procedure_detail.html", {"proc": proc, "procedure": proc})
