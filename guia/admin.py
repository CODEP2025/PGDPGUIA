from django.contrib import admin
from .models import Eixo, Procedimento

@admin.register(Eixo)
class EixoAdmin(admin.ModelAdmin):
    list_display = ("ordem", "nome", "slug")
    list_editable = ("ordem",)
    search_fields = ("nome",)
    prepopulated_fields = {"slug": ("nome",)}

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "eixo")
    list_filter = ("eixo",)
    search_fields = (
        "titulo",
        "o_que_e",
        "quem_tem_direito",
        "documentos_exigidos",
        "procedimentos_passo",
        "base_legal_regimentar",
        "observacoes_praticas",
    )
    prepopulated_fields = {"slug": ("titulo",)}
    fieldsets = (
        (None, {"fields": ("eixo", "titulo", "slug")}),
        ("Conteúdo", {"fields": (
            "o_que_e",
            "quem_tem_direito",
            "documentos_exigidos",
            "procedimentos_passo",
            "base_legal_regimentar",
            "observacoes_praticas",
        )}),
        ("Links", {"fields": ("link_formulario", "texto_link")}),
        ("Metadados", {"fields": ("criado_em", "atualizado_em"), "classes": ("collapse",)}),
    )
    readonly_fields = ("criado_em", "atualizado_em")
