class Backend(object):

    def __init__(self, name: str, dashboard: str, tls_verify: bool = True, skip_login: bool = False, customer_guid: str = None):
        self.name = name
        self.dashboard = dashboard
        self.tls_verify = tls_verify
        self.skip_login = skip_login
        self.customer_guid = customer_guid

    def get_dashboard_url(self):
        return self.dashboard

    def get_name(self):
        return self.name

    def use_tls(self):
        return self.tls_verify
    
    def do_skip_login(self):
        return self.skip_login

    def get_customer_guid(self):
        return self.customer_guid


def set_backends():
    backends = list()

    # development
    backends.append(Backend(name='development',
                            dashboard='https://dashbe.eudev3.cyberarmorsoft.com',
                            tls_verify=False))

    # staging
    backends.append(Backend(name='staging',
                            dashboard='https://dashbe.eustage2.cyberarmorsoft.com'))

    # production
    backends.append(Backend(name='production',
                            dashboard='https://dashbe.euprod1.cyberarmorsoft.com',
                            tls_verify=False))

    # production2 us-east-1
    backends.append(Backend(name='production-us',
                            dashboard='https://dashbe.prod2.us.armo.cloud',
                            tls_verify=False))

    # dev2
    backends.append(Backend(name='dev2',
                            dashboard='https://dashbe.eudev2.cyberarmorsoft.com',
                            tls_verify=False))
    
    # local
    backends.append(Backend(name='local',
                            dashboard='http://localhost:7666',
                            tls_verify=False,
                            skip_login=True,
                            customer_guid="1e3a88bf-92ce-44f8-914e-cbe71830d566"))

    return {backend.get_name(): backend for backend in backends}


BACKENDS = set_backends()
