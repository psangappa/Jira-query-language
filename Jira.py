import requests
import urllib


def get_jira_data(jira_query, server_url, user, password):
    """
    JQL result
    :param jira_query: jql
    :param server_url: url
    :param user: username
    :param password: password
    :return: dict JQL result
    """
    jira_result = {}
    jql = 'search?jql=%s' % urllib.quote(jira_query)
    max_result = "1000"
    starts_at = 0
    total_records = 1001

    # By default, the jql returns maximum of 1000 records at once
    while starts_at < total_records:
        start = "&startAt={}".format(starts_at)
        max = "&maxResults={}".format(max_result)
        response = requests.get(server_url + jql + start + max, verify=False, auth=(user, password))
        if response.status_code != 200:
            return None
        result = response.json()
        total_records = result.get("total", 0)
        starts_at += int(max_result) + 1
        jira_result.update(result)

    start = "&startAt={}".format(starts_at)
    max = "&maxResults={}".format(max_result)
    response = requests.get(server_url + jql + start + max, verify=False, auth=(user, password))
    if response.status_code != 200:
        return None
    result = response.json()
    jira_result.update(result)
    return jira_result


if __name__ == "__main__":
    jira_query = ""  # your jira query here - example: project=xyz and status=closed
    server_url = ""  # jira URL here - example: http://example.com/agile/rest/api/2/
    user = ""  # User name here
    password = ""  # Password here
    jira_query_result = get_jira_data(jira_query, server_url, user, password)