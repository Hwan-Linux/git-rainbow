from django.db import models


class GithubUser(models.Model):
    """
    status types
      requested: Backend sets status to 'requested' before requesting core API
      progress: Core sets status to 'progress' when received analyzing api request
      ready: Core sets status to 'ready' when analyzing devloper finished
      completed: Backend sets status to 'completed' when saved analysis data in tech_stack_analysis_data table
      fail: Core sets status to 'fail' when analyzing devloper failed
    """
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    github_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=260, null=True)
    email = models.EmailField(null=True)
    avatar_url = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True)
    status = models.CharField(max_length=30, null=True)
    updated_date = models.DateTimeField(auto_now=True)


class AnalysisData(models.Model):
    github_id = models.OneToOneField('GithubUser', on_delete=models.CASCADE)
    tech_card_data = models.TextField(null=True)
    git_calendar_data = models.TextField(null=True)


class GithubCalendar(models.Model):
    author_date = models.DateTimeField()
    tech_name = models.CharField(max_length=50)
    lines = models.IntegerField()
    github_id = models.ForeignKey("GithubUser", on_delete=models.CASCADE)


class Ranking(models.Model):
    github_id = models.ForeignKey('GithubUser', on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=50)
    midnight_rank = models.IntegerField()
    updated_date = models.DateTimeField(auto_now=True)
