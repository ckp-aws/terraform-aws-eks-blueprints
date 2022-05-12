import json
import glob
import re


def get_examples():
    """
    Get all Terraform example root directories using their respective `versions.tf`;
    returning a string formatted json array of the example directories minus those that are excluded
    """
    exclude = {
        'examples/eks-cluster-with-external-dns',  # excluded since GitLab auth, backend, etc. required
        'examples/ci-cd/gitlab-ci-cd',  # excluded until Rout53 is setup
        'examples/observability/amp-amg-opensearch',  # TODO - needs to be updated to run example
        'examples/observability/eks-java-jmx'  # TODO - needs to be updated to run example
    }

    projects = {
        x.replace('/versions.tf', '')
        for x in glob.glob('examples/**/versions.tf', recursive=True)
        if not re.match(r'^.+/_', x)
    }

    print(json.dumps(list(projects.difference(exclude))))


if __name__ == '__main__':
    get_examples()