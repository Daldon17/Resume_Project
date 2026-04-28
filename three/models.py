from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # NEW FIELDS (ATS analysis)
    score = models.IntegerField(default=0)
    matched_keywords = models.TextField(blank=True)
    missing_keywords = models.TextField(blank=True)
    experience_score = models.IntegerField(default=0)
    skills_score = models.IntegerField(default=0)
    education_score = models.IntegerField(default=0)
    certifications_score = models.IntegerField(default=0)
    job_title_score = models.IntegerField(default=0)