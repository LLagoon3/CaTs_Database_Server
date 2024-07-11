from django.db import models
from django.db.models import Q, F


class Member(models.Model):
    @staticmethod
    def name():
        return "Member"

    @staticmethod
    def pk_name():
        return "member_id"

    member_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=40)
    join_at = models.DateField(auto_now_add=True)


class Letter(models.Model):
    @staticmethod
    def name():
        return "Letter"

    @staticmethod
    def pk_name():
        return "letter_id"

    letter_id = models.AutoField(primary_key=True)
    sender_id = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="sent_letters"
    )
    receiver_id = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="received_letters"
    )
    image_path = models.CharField(max_length=255)
    sent_at = models.DateField()


class LoverRelationship(models.Model):
    @staticmethod
    def name():
        return "LoverRelationship"

    @staticmethod
    def pk_name():
        return "None"

    member_id1 = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="lover_relationships_1"
    )
    member_id2 = models.OneToOneField(
        Member, on_delete=models.CASCADE, related_name="lover_relationships_2"
    )
    created_at = models.DateField()

    class Meta:
        constraints = [
            # member_id1과 member_id2의 조합이 고유하도록 강제
            models.UniqueConstraint(
                fields=["member_id1", "member_id2"], name="unique_lover_relationships"
            ),
            # member_id1과 member_id2가 같지 않도록 강제
            models.CheckConstraint(
                check=~Q(member_id1=F("member_id2")),
                name="check_lover_different_members",
            ),
        ]


class FamilyRelationship(models.Model):
    @staticmethod
    def name():
        return "FamilyRelationship"

    @staticmethod
    def pk_name():
        return "None"

    member_id1 = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="family_relationships_1"
    )
    member_id2 = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="family_relationships_2"
    )
    created_at = models.DateField()

    class Meta:
        constraints = [
            # member_id1과 member_id2의 조합이 고유하도록 강제
            models.UniqueConstraint(
                fields=["member_id1", "member_id2"], name="unique_family_relationships"
            ),
            # member_id1과 member_id2가 같지 않도록 강제
            models.CheckConstraint(
                check=~Q(member_id1=F("member_id2")),
                name="check_family_different_members",
            ),
        ]

    def save(self, *args, **kwargs):
        # member_id1이 항상 member_id2보다 작도록 정렬
        if self.member_id1_id > self.member_id2_id:
            self.member_id1, self.member_id2 = self.member_id2, self.member_id1
        super(FamilyRelationship, self).save(*args, **kwargs)
