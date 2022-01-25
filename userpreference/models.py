from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    """
    db_index explaination:- 
    This is not really django specific; more to do with databases. You add indexes on columns when
    you want to speed up searches on that column.
    Typically, only the primary key is indexed by the database. This means look ups using the primary
    key are optimized.
    If you do a lot of lookups on a secondary column, consider adding an index to that column to
    speed things up.
    Keep in mind, like most problems of scale, these only apply if you have a statistically large
    number of rows (10,000 is not large).
    Additionally, every time you do an insert, indexes need to be updated. So be careful on which 
    column you add indexes.
    As always, you can only optimize what you can measure - so use the EXPLAIN statement and your
    database logs (especially any slow query logs) to find out where indexes can be useful.
    """

    created_at = models.DateTimeField(default=timezone.now, db_index=True,
                                      verbose_name='Created At')
    modified_at = models.DateTimeField(auto_now=True, db_index=True,
                                       verbose_name='Modified At')

    class Meta:
        abstract = True


class UserPreference(BaseModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Preference = models.CharField(max_length=30)

	def __str__(self):
		return self.Preference


def fetch_userpreferencies(self):
  return UserPreference.objects.filter(user__id=self.id).values_list(
    'Preference', flat=True)

User.add_to_class("fetch_userpreferencies",fetch_userpreferencies)
