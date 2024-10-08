"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_31.core.v1
import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class Event(K8sSpec):
    """Event is a report of an event somewhere in the cluster. It generally denotes some state change in the
    system. Events have a limited retention time and triggers and messages may evolve with time.  Event
    consumers should not rely on the timing of an event with a given Reason reflecting a consistent
    underlying trigger, or the continued existence of events with that Reason.  Events should be treated
    as informative, best-effort, supplemental data.

    Attributes:
        action: action is what action was taken/failed regarding to the regarding object. It is machine-
            readable. This field cannot be empty for new Events and it can have at most 128 characters.
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        deprecatedCount: deprecatedCount is the deprecated field assuring backward compatibility with core.v1
            Event type.
        deprecatedFirstTimestamp: deprecatedFirstTimestamp is the deprecated field assuring backward
            compatibility with core.v1 Event type.
        deprecatedLastTimestamp: deprecatedLastTimestamp is the deprecated field assuring backward
            compatibility with core.v1 Event type.
        deprecatedSource: deprecatedSource is the deprecated field assuring backward compatibility with
            core.v1 Event type.
        eventTime: eventTime is the time when this Event was first observed. It is required.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        note: note is a human-readable description of the status of this operation. Maximal length of the note
            is 1kB, but libraries should be prepared to handle values up to 64kB.
        reason: reason is why the action was taken. It is human-readable. This field cannot be empty for new
            Events and it can have at most 128 characters.
        regarding: regarding contains the object this Event is about. In most cases it's an Object reporting
            controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted
            because it acts on some changes in a ReplicaSet object.
        related: related is the optional secondary object for more complex actions. E.g. when regarding object
            triggers a creation or deletion of related object.
        reportingController: reportingController is the name of the controller that emitted this Event, e.g.
            `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        reportingInstance: reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This
            field cannot be empty for new Events and it can have at most 128 characters.
        series: series is data about the Event series this event represents or nil if it's a singleton Event.
        type: type is the type of this event (Normal, Warning), new types could be added in the future. It is
            machine-readable. This field cannot be empty for new Events.

    """

    eventTime: str
    action: Optional[str] = None
    apiVersion: Optional[str] = None
    deprecatedCount: Optional[int] = None
    deprecatedFirstTimestamp: Optional[str] = None
    deprecatedLastTimestamp: Optional[str] = None
    deprecatedSource: Optional[gybe.k8s.v1_31.core.v1.EventSource] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    note: Optional[str] = None
    reason: Optional[str] = None
    regarding: Optional[gybe.k8s.v1_31.core.v1.ObjectReference] = None
    related: Optional[gybe.k8s.v1_31.core.v1.ObjectReference] = None
    reportingController: Optional[str] = None
    reportingInstance: Optional[str] = None
    series: Optional[EventSeries] = None
    type: Optional[str] = None


@dataclass
class EventList(K8sSpec):
    """EventList is a list of Event objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a list of schema objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Event]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class EventSeries(K8sSpec):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for
    some time. How often to update the EventSeries is up to the event reporters. The default event
    reporter in 'k8s.io/client-go/tools/events/event_broadcaster.go' shows how this struct is updated on
    heartbeats and can guide customized reporter implementations.

    Attributes:
        count: count is the number of occurrences in this series up to the last heartbeat time.
        lastObservedTime: lastObservedTime is the time when last Event from the series was seen before last
            heartbeat.

    """

    count: int
    lastObservedTime: str
