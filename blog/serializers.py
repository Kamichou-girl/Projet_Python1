from rest_framework import serializers
from .models import Categorie, Article, Commentaire
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom']
        ref_name = 'BlogCategorieSerializer'

class ArticleSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    categorie_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(), source='categorie', write_only=True
    )
    auteur = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'categorie', 'categorie_id', 'auteur', 'titre', 'slug',
            'intro', 'image_card', 'image_detail', 'image_banniere',
            'paragraphe_2', 'paragraphe_3', 'paragraphe_4', 'paragraphe_5',
            'date_publication', 'est_publie'
        ]
        ref_name = 'BlogArticleSerializer'

class CommentaireSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source='article', write_only=True
    )
    utilisateur = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Commentaire
        fields = ['id', 'article', 'article_id', 'utilisateur', 'contenu', 'parent', 'date']
        ref_name = 'BlogCommentaireSerializer'
