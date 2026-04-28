# ===== NEW API CODE START =====
from rest_framework import serializers

from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        required=True,
        allow_empty_file=False,
        error_messages={
            "required": 'A PDF resume file is required in the "file" field.',
            "empty": "The uploaded resume file is empty.",
            "invalid": "Upload a valid PDF resume file.",
        },
    )

    class Meta:
        model = Resume
        fields = [
            "id",
            "file",
            "uploaded_at",
            "score",
            "matched_keywords",
            "missing_keywords",
            "experience_score",
            "skills_score",
            "education_score",
            "certifications_score",
            "job_title_score",
        ]
        read_only_fields = [
            "id",
            "uploaded_at",
            "score",
            "matched_keywords",
            "missing_keywords",
            "experience_score",
            "skills_score",
            "education_score",
            "certifications_score",
            "job_title_score",
        ]

    def validate_file(self, value):
        file_name = getattr(value, "name", "")
        if not file_name:
            raise serializers.ValidationError(
                'A PDF resume file is required in the "file" field.'
            )

        if not file_name.lower().endswith(".pdf"):
            raise serializers.ValidationError(
                "Invalid file type. Only .pdf files are allowed."
            )

        return value
# ===== NEW API CODE END =====
