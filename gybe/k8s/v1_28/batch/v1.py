"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_28.core.v1
import gybe.k8s.v1_28.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class CronJob(K8sSpec):
    """CronJob represents the configuration of a single cron job.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of a cron job, including the schedule.
        status: Current status of a cron job.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_28.meta.v1.ObjectMeta] = None
    spec: Optional[CronJobSpec] = None
    status: Optional[CronJobStatus] = None


@dataclass
class CronJobList(K8sSpec):
    """CronJobList is a collection of cron jobs.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of CronJobs.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[CronJob]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class CronJobSpec(K8sSpec):
    """CronJobSpec describes how the job execution will look like and when it will actually run.

    Attributes
    ----------
        concurrencyPolicy: Specifies how to treat concurrent executions of a Job. Valid values are:  - 'Allow'
            (default): allows CronJobs to run concurrently; - 'Forbid': forbids concurrent runs, skipping next
            run if previous run hasn't finished yet; - 'Replace': cancels currently running job and replaces
            it with a new one
        failedJobsHistoryLimit: The number of failed finished jobs to retain. Value must be non-negative
            integer. Defaults to 1.
        jobTemplate: Specifies the job that will be created when executing a CronJob.
        schedule: The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.
        startingDeadlineSeconds: Optional deadline in seconds for starting the job if it misses scheduled time
            for any reason.  Missed jobs executions will be counted as failed ones.
        successfulJobsHistoryLimit: The number of successful finished jobs to retain. Value must be non-
            negative integer. Defaults to 3.
        suspend: This flag tells the controller to suspend subsequent executions, it does not apply to already
            started executions.  Defaults to false.
        timeZone: The time zone name for the given schedule, see
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default
            to the time zone of the kube-controller-manager process. The set of valid time zone names and the
            time zone offset is loaded from the system-wide time zone database by the API server during
            CronJob validation and the controller manager during execution. If no system-wide time zone
            database can be found a bundled version of the database is used instead. If the time zone name
            becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the
            controller will stop creating new new Jobs and will create a system event with the reason
            UnknownTimeZone. More information can be found in
            https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones

    """

    schedule: str
    jobTemplate: JobTemplateSpec
    concurrencyPolicy: Optional[str] = None
    failedJobsHistoryLimit: Optional[int] = None
    startingDeadlineSeconds: Optional[int] = None
    successfulJobsHistoryLimit: Optional[int] = None
    suspend: Optional[bool] = None
    timeZone: Optional[str] = None


@dataclass
class CronJobStatus(K8sSpec):
    """CronJobStatus represents the current state of a cron job.

    Attributes
    ----------
        active: A list of pointers to currently running jobs.
        lastScheduleTime: Information when was the last time the job was successfully scheduled.
        lastSuccessfulTime: Information when was the last time the job successfully completed.

    """

    active: Optional[List[gybe.k8s.v1_28.core.v1.ObjectReference]] = None
    lastScheduleTime: Optional[str] = None
    lastSuccessfulTime: Optional[str] = None


@dataclass
class Job(K8sSpec):
    """Job represents the configuration of a single job.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of a job.
        status: Current status of a job.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_28.meta.v1.ObjectMeta] = None
    spec: Optional[JobSpec] = None
    status: Optional[JobStatus] = None


@dataclass
class JobCondition(K8sSpec):
    """JobCondition describes current state of a job.

    Attributes
    ----------
        lastProbeTime: Last time the condition was checked.
        lastTransitionTime: Last time the condition transit from one status to another.
        message: Human readable message indicating details about last transition.
        reason: (brief) reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of job condition, Complete or Failed.

    """

    type: str
    status: str
    lastProbeTime: Optional[str] = None
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class JobList(K8sSpec):
    """JobList is a collection of jobs.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of Jobs.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Job]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class JobSpec(K8sSpec):
    """JobSpec describes how the job execution will look like.

    Attributes
    ----------
        activeDeadlineSeconds: Specifies the duration in seconds relative to the startTime that the job may be
            continuously active before the system tries to terminate it; value must be positive integer. If a
            Job is suspended (at creation or through an update), this timer will effectively be stopped and
            reset when the Job is resumed again.
        backoffLimit: Specifies the number of retries before marking this job failed. Defaults to 6
        backoffLimitPerIndex: Specifies the limit for the number of retries within an index before marking
            this index as failed. When enabled the number of failures per index is kept in the pod's
            batch.kubernetes.io/job-index-failure-count annotation. It can only be set when Job's
            completionMode=Indexed, and the Pod's restart policy is Never. The field is immutable. This field
            is alpha-level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled
            (disabled by default).
        completionMode: completionMode specifies how Pod completions are tracked. It can be `NonIndexed`
            (default) or `Indexed`.  `NonIndexed` means that the Job is considered complete when there have
            been .spec.completions successfully completed Pods. Each Pod completion is homologous to each
            other.  `Indexed` means that the Pods of a Job get an associated completion index from 0 to
            (.spec.completions - 1), available in the annotation batch.kubernetes.io/job-completion-index. The
            Job is considered complete when there is one successfully completed Pod for each index. When value
            is `Indexed`, .spec.completions must be specified and `.spec.parallelism` must be less than or
            equal to 10^5. In addition, The Pod name takes the form `$(job-name)-$(index)-$(random-string)`,
            the Pod hostname takes the form `$(job-name)-$(index)`.  More completion modes can be added in the
            future. If the Job controller observes a mode that it doesn't recognize, which is possible during
            upgrades due to version skew, the controller skips updates for the Job.
        completions: Specifies the desired number of successfully finished pods the job should be run with.
            Setting to null means that the success of any pod signals the success of all pods, and allows
            parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and
            the success of that pod signals the success of the job.
        manualSelector: manualSelector controls generation of pod labels and pod selectors. Leave
            `manualSelector` unset unless you are certain what you are doing. When false or unset, the system
            pick labels unique to this job and appends those labels to the pod template.  When true, the user
            is responsible for picking unique labels and specifying the selector.  Failure to pick a unique
            label may cause this and other jobs to not function correctly.  However, You may see
            `manualSelector=true` in jobs that were created with the old `extensions/v1beta1` API.
        maxFailedIndexes: Specifies the maximal number of failed indexes before marking the Job as failed,
            when backoffLimitPerIndex is set. Once the number of failed indexes exceeds this number the entire
            Job is marked as Failed and its execution is terminated. When left as null the job continues
            execution of all of its indexes and is marked with the `Complete` Job condition. It can only be
            specified when backoffLimitPerIndex is set. It can be null or up to completions. It is required
            and must be less than or equal to 10^4 when is completions greater than 10^5. This field is alpha-
            level. It can be used when the `JobBackoffLimitPerIndex` feature gate is enabled (disabled by
            default).
        parallelism: Specifies the maximum desired number of pods the job should run at any given time. The
            actual number of pods running in steady state will be less than this number when
            ((.spec.completions - .status.successful) < .spec.parallelism), i.e. when the work left to do is
            less than max parallelism.
        podFailurePolicy: Specifies the policy of handling failed pods. In particular, it allows to specify
            the set of actions and conditions which need to be satisfied to take the associated action. If
            empty, the default behaviour applies - the counter of failed pods, represented by the jobs's
            .status.failed field, is incremented and it is checked against the backoffLimit. This field cannot
            be used in combination with restartPolicy=OnFailure.  This field is beta-level. It can be used
            when the `JobPodFailurePolicy` feature gate is enabled (enabled by default).
        podReplacementPolicy: podReplacementPolicy specifies when to create replacement Pods. Possible values
            are: - TerminatingOrFailed means that we recreate pods   when they are terminating (has a
            metadata.deletionTimestamp) or failed. - Failed means to wait until a previously created Pod is
            fully terminated (has phase   Failed or Succeeded) before creating a replacement Pod.  When using
            podFailurePolicy, Failed is the the only allowed value. TerminatingOrFailed and Failed are allowed
            values when podFailurePolicy is not in use. This is an alpha field. Enable JobPodReplacementPolicy
            to be able to use this field.
        selector: A label query over pods that should match the pod count. Normally, the system sets this
            field for you.
        suspend: suspend specifies whether the Job controller should create Pods or not. If a Job is created
            with suspend set to true, no Pods are created by the Job controller. If a Job is suspended after
            creation (i.e. the flag goes from false to true), the Job controller will delete all active Pods
            associated with this Job. Users must design their workload to gracefully handle this. Suspending a
            Job will reset the StartTime field of the Job, effectively resetting the ActiveDeadlineSeconds
            timer too. Defaults to false.
        template: Describes the pod that will be created when executing a job. The only allowed
            template.spec.restartPolicy values are 'Never' or 'OnFailure'.
        ttlSecondsAfterFinished: ttlSecondsAfterFinished limits the lifetime of a Job that has finished
            execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job
            finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle
            guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won't be
            automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted
            immediately after it finishes.

    """

    template: gybe.k8s.v1_28.core.v1.PodTemplateSpec
    activeDeadlineSeconds: Optional[int] = None
    backoffLimit: Optional[int] = None
    backoffLimitPerIndex: Optional[int] = None
    completionMode: Optional[str] = None
    completions: Optional[int] = None
    manualSelector: Optional[bool] = None
    maxFailedIndexes: Optional[int] = None
    parallelism: Optional[int] = None
    podFailurePolicy: Optional[PodFailurePolicy] = None
    podReplacementPolicy: Optional[str] = None
    selector: Optional[gybe.k8s.v1_28.meta.v1.LabelSelector] = None
    suspend: Optional[bool] = None
    ttlSecondsAfterFinished: Optional[int] = None


@dataclass
class JobStatus(K8sSpec):
    """JobStatus represents the current state of a Job.

    Attributes
    ----------
        active: The number of pending and running pods.
        completedIndexes: completedIndexes holds the completed indexes when .spec.completionMode = 'Indexed'
            in a text format. The indexes are represented as decimal integers separated by commas. The numbers
            are listed in increasing order. Three or more consecutive numbers are compressed and represented
            by the first and last element of the series, separated by a hyphen. For example, if the completed
            indexes are 1, 3, 4, 5 and 7, they are represented as '1,3-5,7'.
        completionTime: Represents time when the job was completed. It is not guaranteed to be set in happens-
            before order across separate operations. It is represented in RFC3339 form and is in UTC. The
            completion time is only set when the job finishes successfully.
        conditions: The latest available observations of an object's current state. When a Job fails, one of
            the conditions will have type 'Failed' and status true. When a Job is suspended, one of the
            conditions will have type 'Suspended' and status true; when the Job is resumed, the status of this
            condition will become false. When a Job is completed, one of the conditions will have type
            'Complete' and status true.
        failed: The number of pods which reached phase Failed.
        failedIndexes: FailedIndexes holds the failed indexes when backoffLimitPerIndex=true. The indexes are
            represented in the text format analogous as for the `completedIndexes` field, ie. they are kept as
            decimal integers separated by commas. The numbers are listed in increasing order. Three or more
            consecutive numbers are compressed and represented by the first and last element of the series,
            separated by a hyphen. For example, if the failed indexes are 1, 3, 4, 5 and 7, they are
            represented as '1,3-5,7'. This field is alpha-level. It can be used when the
            `JobBackoffLimitPerIndex` feature gate is enabled (disabled by default).
        ready: The number of pods which have a Ready condition.  This field is beta-level. The job controller
            populates the field when the feature gate JobReadyPods is enabled (enabled by default).
        startTime: Represents time when the job controller started processing a job. When a Job is created in
            the suspended state, this field is not set until the first time it is resumed. This field is reset
            every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.
        succeeded: The number of pods which reached phase Succeeded.
        terminating: The number of pods which are terminating (in phase Pending or Running and have a
            deletionTimestamp).  This field is alpha-level. The job controller populates the field when the
            feature gate JobPodReplacementPolicy is enabled (disabled by default).
        uncountedTerminatedPods: uncountedTerminatedPods holds the UIDs of Pods that have terminated but the
            job controller hasn't yet accounted for in the status counters.  The job controller creates pods
            with a finalizer. When a pod terminates (succeeded or failed), the controller does three steps to
            account for it in the job status:  1. Add the pod UID to the arrays in this field. 2. Remove the
            pod finalizer. 3. Remove the pod UID from the arrays while increasing the corresponding
            counter.  Old jobs might not be tracked using this field, in which case the field remains null.

    """

    active: Optional[int] = None
    completedIndexes: Optional[str] = None
    completionTime: Optional[str] = None
    conditions: Optional[List[JobCondition]] = None
    failed: Optional[int] = None
    failedIndexes: Optional[str] = None
    ready: Optional[int] = None
    startTime: Optional[str] = None
    succeeded: Optional[int] = None
    terminating: Optional[int] = None
    uncountedTerminatedPods: Optional[UncountedTerminatedPods] = None


@dataclass
class JobTemplateSpec(K8sSpec):
    """JobTemplateSpec describes the data a Job should have when created from a template
    Attributes:
        metadata: Standard object's metadata of the jobs created from this template.
        spec: Specification of the desired behavior of the job.

    """

    metadata: Optional[gybe.k8s.v1_28.meta.v1.ObjectMeta] = None
    spec: Optional[JobSpec] = None


@dataclass
class PodFailurePolicy(K8sSpec):
    """PodFailurePolicy describes how failed pods influence the backoffLimit.

    Attributes
    ----------
        rules: A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod
            failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default
            handling applies - the counter of pod failures is incremented and it is checked against the
            backoffLimit. At most 20 elements are allowed.

    """

    rules: List[PodFailurePolicyRule]


@dataclass
class PodFailurePolicyOnExitCodesRequirement(K8sSpec):
    """PodFailurePolicyOnExitCodesRequirement describes the requirement for handling a failed pod based on
    its container exit codes. In particular, it lookups the .state.terminated.exitCode for each app
    container and init container status, represented by the .status.containerStatuses and
    .status.initContainerStatuses fields in the Pod status, respectively. Containers completed with
    success (exit code 0) are excluded from the requirement check.

    Attributes
    ----------
        containerName: Restricts the check for exit codes to the container with the specified name. When null,
            the rule applies to all containers. When specified, it should match one the container or
            initContainer names in the pod template.
        operator: Represents the relationship between the container exit code(s) and the specified values.
            Containers completed with success (exit code 0) are excluded from the requirement check. Possible
            values are:  - In: the requirement is satisfied if at least one container exit code   (might be
            multiple if there are multiple containers not restricted   by the 'containerName' field) is in the
            set of specified values. - NotIn: the requirement is satisfied if at least one container exit code
            (might be multiple if there are multiple containers not restricted   by the 'containerName' field)
            is not in the set of specified values. Additional values are considered to be added in the future.
            Clients should react to an unknown operator by assuming the requirement is not satisfied.
        values: Specifies the set of values. Each returned container exit code (might be multiple in case of
            multiple containers) is checked against this set of values with respect to the operator. The list
            of values must be ordered and must not contain duplicates. Value '0' cannot be used for the In
            operator. At least one element is required. At most 255 elements are allowed.

    """

    operator: str
    values: List[int]
    containerName: Optional[str] = None


@dataclass
class PodFailurePolicyOnPodConditionsPattern(K8sSpec):
    """PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.

    Attributes
    ----------
        status: Specifies the required Pod condition status. To match a pod condition it is required that the
            specified status equals the pod condition status. Defaults to True.
        type: Specifies the required Pod condition type. To match a pod condition it is required that
            specified type equals the pod condition type.

    """

    type: str
    status: str


@dataclass
class PodFailurePolicyRule(K8sSpec):
    """PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of
    onExitCodes and onPodConditions, but not both, can be used in each rule.

    Attributes
    ----------
        action: Specifies the action taken on a pod failure when the requirements are satisfied. Possible
            values are:  - FailJob: indicates that the pod's job is marked as Failed and all   running pods
            are terminated. - FailIndex: indicates that the pod's index is marked as Failed and will   not be
            restarted.   This value is alpha-level. It can be used when the   `JobBackoffLimitPerIndex`
            feature gate is enabled (disabled by default). - Ignore: indicates that the counter towards the
            .backoffLimit is not   incremented and a replacement pod is created. - Count: indicates that the
            pod is handled in the default way - the   counter towards the .backoffLimit is incremented.
            Additional values are considered to be added in the future. Clients should react to an unknown
            action by skipping the rule.
        onExitCodes: Represents the requirement on the container exit codes.
        onPodConditions: Represents the requirement on the pod conditions. The requirement is represented as a
            list of pod condition patterns. The requirement is satisfied if at least one pattern matches an
            actual pod condition. At most 20 elements are allowed.

    """

    action: str
    onExitCodes: Optional[PodFailurePolicyOnExitCodesRequirement] = None
    onPodConditions: Optional[List[PodFailurePolicyOnPodConditionsPattern]] = None


@dataclass
class UncountedTerminatedPods(K8sSpec):
    """UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job
    status counters.

    Attributes
    ----------
        failed: failed holds UIDs of failed Pods.
        succeeded: succeeded holds UIDs of succeeded Pods.

    """

    failed: Optional[List[str]] = None
    succeeded: Optional[List[str]] = None
