# Generated by Django 4.1.7 on 2023-03-18 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_attestation_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attestation',
            name='profile',
        ),
        migrations.AddField(
            model_name='attestation',
            name='cin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attestations_cin', to='app.profile'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='cne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attestations_cne', to='app.profile'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='nom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attestations_nom', to='app.profile'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='prenom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attestations_prenom', to='app.profile'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
