from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent


class AppConfig(EdcRegistrationAppConfigParent):
    model = ('example_registration', 'registeredsubject')
