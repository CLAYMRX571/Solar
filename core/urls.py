"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.about.views import Aboutviews, lan_switch_about
from apps.achievement.views import Achievementviews, lan_switch_achievement
from apps.advance.views import Advanceviews, lan_switch_advance
from apps.award.views import Awardviews, lan_switch_award
from apps.board.views import Boardviews, lan_switch_board
from apps.challenge.views import Challengeviews, lan_switch_challenge
from apps.column.views import Columnviews, lan_switch_column
from apps.conference.views import Conferenceviews, lan_switch_conference
from apps.contact.views import Contactviews, lan_switch_contact
from apps.daniel.views import Danielviews, lan_switch_daniel
from apps.eurosun.views import Eurosunviews, lan_switch_eurosun
from apps.event.views import Eventviews, lan_switch_event
from apps.fellow.views import Fellowviews, lan_switch_fellow
from apps.history.views import Historyviews, lan_switch_history
from apps.home.views import Homeviews, lan_switch
from apps.incore.views import Incoreviews, lan_switch_incore
from apps.jobs.views import Jobsviews, lan_switch_jobs
from apps.journal.views import Journalviews, lan_switch_journal
from apps.leader.views import Leaderviews, lan_switch_leader
from apps.membership.views import Membershipviews, lan_switch_membership
from apps.museum.views import Museumviews, lan_switch_museum
from apps.news.views import Newsviews, lan_switch_news
from apps.part.views import Partviews, lan_switch_part
from apps.public.views import Publicviews, lan_switch_public
from apps.structure.views import Structureviews, lan_switch_structure
from apps.support.views import Supportviews, lan_switch_support
from apps.team.views import Teamviews, lan_switch_team
from apps.webinar.views import Webinarviews, lan_switch_webinar
from apps.young.views import Youngviews, lan_switch_young

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('lan/about/<str:lan>/', lan_switch_about, name='lan_switch_about'),
    path('lan/achievement/<str:lan>/', lan_switch_achievement, name='lan_switch_achievement'),
    path('lan/advance/<str:lan>/', lan_switch_advance, name='lan_switch_advance'),
    path('lan/award/<str:lan>/', lan_switch_award, name='lan_switch_award'),
    path('lan/board/<str:lan>/', lan_switch_board, name='lan_switch_board'),
    path('lan/challenge/<str:lan>/', lan_switch_challenge, name='lan_switch_challenge'),
    path('lan/column/<str:lan>/', lan_switch_column, name='lan_switch_column'),
    path('lan/conference/<str:lan>/', lan_switch_conference, name='lan_switch_conference'),
    path('lan/contact/<str:lan>/', lan_switch_contact, name='lan_switch_contact'),
    path('lan/daniel/<str:lan>/', lan_switch_daniel, name='lan_switch_daniel'),
    path('lan/eurosun/<str:lan>/', lan_switch_eurosun, name='lan_switch_eurosun'),
    path('lan/event/<str:lan>/', lan_switch_event, name='lan_switch_event'),
    path('lan/fellow/<str:lan>/', lan_switch_fellow, name='lan_switch_fellow'),
    path('lan/history/<str:lan>/', lan_switch_history, name='lan_switch_history'),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/incore/<str:lan>/', lan_switch_incore, name='lan_switch_incore'),
    path('lan/jobs/<str:lan>/', lan_switch_jobs, name='lan_switch_jobs'),
    path('lan/journal/<str:lan>/', lan_switch_journal, name='lan_switch_journal'),
    path('lan/leader/<str:lan>/', lan_switch_leader, name='lan_switch_leader'),
    path('lan/membership/<str:lan>/', lan_switch_membership, name='lan_switch_membership'),
    path('lan/museum/<str:lan>/', lan_switch_museum, name='lan_switch_museum'),
    path('lan/news/<str:lan>/', lan_switch_news, name='lan_switch_news'),
    path('lan/part/<str:lan>/', lan_switch_part, name='lan_switch_part'),
    path('lan/public/<str:lan>/', lan_switch_public, name='lan_switch_public'),
    path('lan/structure/<str:lan>/', lan_switch_structure, name='lan_switch_structure'),
    path('lan/support/<str:lan>/', lan_switch_support, name='lan_switch_support'),
    path('lan/team/<str:lan>/', lan_switch_team, name='lan_switch_team'),
    path('lan/webinar/<str:lan>/', lan_switch_webinar, name='lan_switch_webinar'),
    path('lan/young/<str:lan>/', lan_switch_young, name='lan_switch_young'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('about/', Aboutviews, name='about'),
    path('achievement/', Achievementviews, name='achievement'),
    path('advance/', Advanceviews, name='advance'),
    path('award/', Awardviews, name='award'),
    path('board/', Boardviews, name='board'),
    path('challenge/', Challengeviews, name='challenge'),
    path('column/', Columnviews, name='column'),
    path('conference/', Conferenceviews, name='conference'),
    path('contact/', Contactviews, name='contact'),
    path('daniel/', Danielviews, name='daniel'),
    path('eurosun/', Eurosunviews, name='eurosun'),
    path('event/', Eventviews, name='event'),
    path('fellow/', Fellowviews, name='fellow'),
    path('history/', Historyviews, name='history'),
    path('', Homeviews, name='index'),
    path('incore/', Incoreviews, name='incore'),
    path('jobs/', Jobsviews, name='jobs'),
    path('journal/', Journalviews, name='journal'),
    path('leader/', Leaderviews, name='leader'),
    path('membership/', Membershipviews, name='membership'),
    path('museum/', Museumviews, name='museum'),
    path('news/', Newsviews, name='news'),
    path('part/', Partviews, name='part'),
    path('public/', Publicviews, name='public'),
    path('structure/', Structureviews, name='structure'),
    path('support/', Supportviews, name='support'),
    path('team/', Teamviews, name='team'),
    path('webinar/', Webinarviews, name='webinar'),
    path('young/', Youngviews, name='young'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)