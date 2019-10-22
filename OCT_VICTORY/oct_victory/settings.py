"""
Django settings for oct_victory project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b9s%!p)l_$18rvsz4rqb=0avv7xt5+)2^%#b$kn2a3=#6y8buy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'board',

    'django_extensions',  # shell_plus 를 주로 많이 씀, ipython도 사용

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oct_victory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # render(request, 'HERE') HERE 파일 찾을 때, 어떤 폴더를 들여다 볼 것인지?
            # 기본 default 로 installed_apps에 등록된 APP/templates/ 안을 찾는다
            # 추가적으로 여기(PROJECT/templates/)도 찾아주세요
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oct_victory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
# 저장되는 DateTimeField의 값이 바뀌는 것이 아닌, 표시되는 시간이 바뀌는 것
# datetimefield에는 기본적으로 UTC로 등록되지만, Asia/Seoul로 보.여.지.는.것
TIME_ZONE = 'Asia/Seoul'  

# 국제화 대응(I nternationalizatio N)
USE_I18N = True

# 현지화 대응(L ocalizatio N)
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static files == 서버가 쓰려고 준비한 파일(CSS, JS, IMAGES) - 빌트인 가구같은 개념
# 우리 서버에서 static 파일을 제공할 때, 필요한 URL 접두사(/static/ 의미 중요하지 않음)
STATIC_URL = '/static/'

# ★★★중요★★★ 우리가 static files를 둘 곳(스펠링 유의!)
STATICFILES_DIRS = [
    # {% static 'HERE' %} HERE 파일 찾을 때, 어떤 폴더를 들여다 볼 것인지?
    # 기본 default 로 installed_apps에 등록된 APP/static/ 안을 찾는다
    # 추가적으로 여기(PROJECT/assets/)도 찾아주세요
    os.path.join(BASE_DIR, 'assets'),
]

# mediafiles == 클라이언트가 업로드하는 파일(*.*) - 사용자 맘대로 올리는 것
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')