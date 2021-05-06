from django.db import models
from django.contrib.postgres.fields import ArrayField

## Django signal Import
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

## Questions taken from the domain recruiters and pushed into database of this model.
## Both for Form responses and form filling frontend (questions and options) can be taken from here to display.
class QuestionsForRecruitment(models.Model):
    CHOICES_QTYPE = [
        ('SingleChoice', 'SingleChoice'),
        ('MultipleChoice', 'MultipleChoice'),
        ('Answer', 'Answer'),
    ]

    CHOICES_DOMAIN = [
        ('Web', 'Web'),
        ('Core', 'Core'),
        ('Design', 'Design'),
        ('Docs', 'Docs'),
        ('PR', 'PR'),
    ]

    question  = models.CharField(max_length=1000)
    question_type  = models.CharField(max_length=1000, choices=CHOICES_QTYPE)
    question_for_domain  = models.CharField(max_length=1000, choices=CHOICES_DOMAIN)
    option1 = models.CharField(max_length=1000, blank=True, null=True)
    option2 = models.CharField(max_length=1000, blank=True, null=True)
    option3 = models.CharField(max_length=1000, blank=True, null=True)
    option4 = models.CharField(max_length=1000, blank=True, null=True)




## Every candidates responses 
class FormResponses(models.Model):
    candidate_name = models.CharField(max_length=1000)
    candidate_mobile_number = models.CharField(max_length=10)
    candidate_emailid = models.EmailField()
    candidate_domain_choices = ArrayField(models.CharField(max_length=100, blank=True),size=2)      ## Limiting the choices to only two.

    ## The Submitted responses for Questions open to all domains
    question_all1 = models.CharField(max_length=1000)
    question_all2 = models.CharField(max_length=1000)
    question_all3 = models.CharField(max_length=1000)
    question_all4 = models.CharField(max_length=1000)
    question_all5 = models.CharField(max_length=1000)
    question_all6 = models.CharField(max_length=1000)

    ## The Submitted responses for Questions only to Web domain
    question_web1 = models.CharField(max_length=1000, blank=True, null=True)
    question_web2 = models.CharField(max_length=1000, blank=True, null=True)
    question_web3 = models.CharField(max_length=1000, blank=True, null=True)
    question_web4 = models.CharField(max_length=1000, blank=True, null=True)
    question_web5 = models.CharField(max_length=1000, blank=True, null=True)
    question_web6 = models.CharField(max_length=1000, blank=True, null=True)


    ## The Submitted responses for Questions only to Core domain
    question_core1 = models.CharField(max_length=1000, blank=True, null=True)
    question_core2 = models.CharField(max_length=1000, blank=True, null=True)
    question_core3 = models.CharField(max_length=1000, blank=True, null=True)
    question_core4 = models.CharField(max_length=1000, blank=True, null=True)
    question_core5 = models.CharField(max_length=1000, blank=True, null=True)
    question_core6 = models.CharField(max_length=1000, blank=True, null=True)


    ## The Submitted responses for Questions only to Design domain
    question_design1 = models.CharField(max_length=1000, blank=True, null=True)
    question_design2 = models.CharField(max_length=1000, blank=True, null=True)
    question_design3 = models.CharField(max_length=1000, blank=True, null=True)
    question_design4 = models.CharField(max_length=1000, blank=True, null=True)
    question_design5 = models.CharField(max_length=1000, blank=True, null=True)
    question_design6 = models.CharField(max_length=1000, blank=True, null=True)

    ## The Submitted responses for Questions only to Docs domain
    question_docs1 = models.CharField(max_length=1000, blank=True, null=True)
    question_docs2 = models.CharField(max_length=1000, blank=True, null=True)
    question_docs3 = models.CharField(max_length=1000, blank=True, null=True)
    question_docs4 = models.CharField(max_length=1000, blank=True, null=True)
    question_docs5 = models.CharField(max_length=1000, blank=True, null=True)
    question_docs6 = models.CharField(max_length=1000, blank=True, null=True)

    ## The Submitted responses for Questions only to PR domain
    question_pr1 = models.CharField(max_length=1000, blank=True, null=True)
    question_pr2 = models.CharField(max_length=1000, blank=True, null=True)
    question_pr3 = models.CharField(max_length=1000, blank=True, null=True)
    question_pr4 = models.CharField(max_length=1000, blank=True, null=True)
    question_pr5 = models.CharField(max_length=1000, blank=True, null=True)
    question_pr6 = models.CharField(max_length=1000, blank=True, null=True)




## Saving the emails and phone numbers to Global level Email and Phone number DB
# @receiver(post_save,sender=FormResponses)
# def img_handler(created,instance,*args,**kwargs):
#     if created:
#         ## For Global level Email save
#         pass