from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(
                    choices=[('education', '🎓 Educación'), ('course', '📚 Curso'),
                             ('cert', '🏆 Certificación'), ('experience', '💼 Experiencia')],
                    default='course', max_length=20, verbose_name='Tipo')),
                ('title',       models.CharField(max_length=200, verbose_name='Título')),
                ('institution', models.CharField(max_length=200, verbose_name='Institución / Plataforma')),
                ('period',      models.CharField(max_length=50,  verbose_name='Período')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('tags',        models.CharField(blank=True, max_length=300, verbose_name='Etiquetas')),
                ('certificate_pdf', models.FileField(
                    blank=True, null=True,
                    upload_to='certificates/',
                    verbose_name='Certificado PDF')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('order',     models.PositiveIntegerField(default=0, verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'Formación / Experiencia',
                'verbose_name_plural': 'Formación y Experiencia',
                'ordering': ['order', '-period'],
            },
        ),
    ]
