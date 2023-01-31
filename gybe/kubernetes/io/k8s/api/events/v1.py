from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1 as v1_1


class EventSeries(BaseModel):
    count: int = Field(
        ...,
        description=(
            "count is the number of occurrences in this series up to the last heartbeat"
            " time."
        ),
    )
    lastObservedTime: v1.MicroTime = Field(
        ...,
        description=(
            "lastObservedTime is the time when last Event from the series was seen"
            " before last heartbeat."
        ),
    )


class Event(BaseModel):
    action: Optional[str] = Field(
        None,
        description=(
            "action is what action was taken/failed regarding to the regarding object."
            " It is machine-readable. This field cannot be empty for new Events and it"
            " can have at most 128 characters."
        ),
    )
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    deprecatedCount: Optional[int] = Field(
        None,
        description=(
            "deprecatedCount is the deprecated field assuring backward compatibility"
            " with core.v1 Event type."
        ),
    )
    deprecatedFirstTimestamp: Optional[v1.Time] = Field(
        None,
        description=(
            "deprecatedFirstTimestamp is the deprecated field assuring backward"
            " compatibility with core.v1 Event type."
        ),
    )
    deprecatedLastTimestamp: Optional[v1.Time] = Field(
        None,
        description=(
            "deprecatedLastTimestamp is the deprecated field assuring backward"
            " compatibility with core.v1 Event type."
        ),
    )
    deprecatedSource: Optional[v1_1.EventSource] = Field(
        None,
        description=(
            "deprecatedSource is the deprecated field assuring backward compatibility"
            " with core.v1 Event type."
        ),
    )
    eventTime: v1.MicroTime = Field(
        ...,
        description=(
            "eventTime is the time when this Event was first observed. It is required."
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
    note: Optional[str] = Field(
        None,
        description=(
            "note is a human-readable description of the status of this operation."
            " Maximal length of the note is 1kB, but libraries should be prepared to"
            " handle values up to 64kB."
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            "reason is why the action was taken. It is human-readable. This field"
            " cannot be empty for new Events and it can have at most 128 characters."
        ),
    )
    regarding: Optional[v1_1.ObjectReference] = Field(
        None,
        description=(
            "regarding contains the object this Event is about. In most cases it's an"
            " Object reporting controller implements, e.g. ReplicaSetController"
            " implements ReplicaSets and this event is emitted because it acts on some"
            " changes in a ReplicaSet object."
        ),
    )
    related: Optional[v1_1.ObjectReference] = Field(
        None,
        description=(
            "related is the optional secondary object for more complex actions. E.g."
            " when regarding object triggers a creation or deletion of related object."
        ),
    )
    reportingController: Optional[str] = Field(
        None,
        description=(
            "reportingController is the name of the controller that emitted this Event,"
            " e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events."
        ),
    )
    reportingInstance: Optional[str] = Field(
        None,
        description=(
            "reportingInstance is the ID of the controller instance, e.g."
            " `kubelet-xyzf`. This field cannot be empty for new Events and it can have"
            " at most 128 characters."
        ),
    )
    series: Optional[EventSeries] = Field(
        None,
        description=(
            "series is data about the Event series this event represents or nil if it's"
            " a singleton Event."
        ),
    )
    type: Optional[str] = Field(
        None,
        description=(
            "type is the type of this event (Normal, Warning), new types could be added"
            " in the future. It is machine-readable. This field cannot be empty for new"
            " Events."
        ),
    )


class EventList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[Event] = Field(..., description="items is a list of schema objects.")
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
