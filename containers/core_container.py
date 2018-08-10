from dependency_injector import containers, providers


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
