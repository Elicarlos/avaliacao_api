from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Servico(BaseModel):
    nome =  models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Avaliacao(BaseModel):
    servico_id = models.ForeignKey(Servico, on_delete=models.CASCADE)
    pontuacao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comentario = models.TextField()
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação para {self.servico.nome} - Pontuação: {self.pontuacao}"
    