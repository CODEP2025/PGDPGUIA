from django.db import models
from django.utils.text import slugify

class Eixo(models.Model):
    nome = models.CharField("Nome do Eixo", max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    descricao = models.TextField("Descrição", blank=True)
    ordem = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        ordering = ["ordem", "nome"]
        verbose_name = "Eixo"
        verbose_name_plural = "Eixos"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class Procedimento(models.Model):
    eixo = models.ForeignKey(Eixo, on_delete=models.PROTECT, related_name="procedimentos")
    titulo = models.CharField("Título", max_length=255)
    slug = models.SlugField(unique=True)

    # Campos estruturados conforme os anexos do PGDP
    o_que_e = models.TextField("O que é", blank=True)
    quem_tem_direito = models.TextField("Quem tem direito", blank=True)
    documentos_exigidos = models.TextField("Documentos exigidos", blank=True)
    procedimentos_passo = models.TextField("Procedimentos (passo a passo)", blank=True)
    base_legal_regimentar = models.TextField("Base legal/regimentar", blank=True)
    observacoes_praticas = models.TextField("Observações práticas", blank=True)

    # Links úteis (ex.: SEI/UNEB – Formulário RDV)
    link_formulario = models.URLField("Link do formulário/SEI", blank=True)
    texto_link = models.CharField("Texto do botão", max_length=255, blank=True, default="Abrir no SEI/UNEB – Formulário RDV")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Procedimento"
        verbose_name_plural = "Procedimentos"

    def __str__(self):
        return self.titulo
