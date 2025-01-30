"""Defines the core protocols that standardize how plugins interact with gybe."""

from typing import Protocol, Sequence

from gybe import k8s


class Chart(Protocol):
    """A standard protocol to expose kubernetes resources to gybe."""

    @property
    def k8s_resources(self) -> Sequence[k8s.K8sResource]:
        """Returns a sequence of Kubernetes resources that make up this chart.

        The property should return all Kubernetes resources required for the chart's
        deployment, such as Deployments, Services, ConfigMaps, etc.
        """
        ...
