from dependency_injector import containers, providers
import application


class Application(containers.DeclarativeContainer):
    main = providers.Callable(application.main)
