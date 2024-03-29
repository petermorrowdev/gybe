from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class PriorityClass(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    description: Optional[str] = Field(
        None,
        description=(
            "description is an arbitrary string that usually provides guidelines on"
            " when this priority class should be used."
        ),
    )
    globalDefault: Optional[bool] = Field(
        None,
        description=(
            "globalDefault specifies whether this PriorityClass should be considered as"
            " the default priority for pods that do not have any priority class. Only"
            " one PriorityClass can be marked as `globalDefault`. However, if more than"
            " one PriorityClasses exists with their `globalDefault` field set to true,"
            " the smallest value of such global default PriorityClasses will be used as"
            " the default priority."
        ),
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    preemptionPolicy: Optional[str] = Field(
        None,
        description=(
            "preemptionPolicy is the Policy for preempting pods with lower priority."
            " One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if"
            " unset."
        ),
    )
    value: int = Field(
        ...,
        description=(
            "value represents the integer value of this priority class. This is the"
            " actual priority that pods receive when they have the name of this class"
            " in their pod spec."
        ),
    )


class PriorityClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[PriorityClass] = Field(
        ..., description="items is the list of PriorityClasses"
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description=(
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
