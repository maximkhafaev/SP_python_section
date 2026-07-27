import requests


class ProjectsApi:

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_authorization(self):
        auth_header = {
            'Authorization': 'Bearer ' + self.token
        }
        return auth_header

    def create_project(self, title):
        auth = self.get_authorization()
        body = {
            'title': title
        }
        create_req = requests.post(self.url + '/api-v2/projects',
                                   headers=auth, json=body)
        return create_req.json(), create_req.status_code

    def get_project_list(self):
        auth = self.get_authorization()
        get_list_req = requests.get(self.url + '/api-v2/projects',
                                    headers=auth)
        return get_list_req.json()

    def get_project_by_id(self, id):
        auth = self.get_authorization()
        get_req = requests.get(self.url + '/api-v2/projects/' + str(id),
                               headers=auth)
        return get_req.json(), get_req.status_code

    def change_project(self, id, title):
        auth = self.get_authorization()
        body = {
            'title': title
        }
        change_req = requests.put(self.url + '/api-v2/projects/' + str(id),
                                  headers=auth, json=body)
        return change_req.json(), change_req.status_code
