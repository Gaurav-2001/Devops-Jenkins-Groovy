job('job1-create web deployment') {
    steps {
        shell('bash /task6_code/job1.sh')
    }
}
job('job2-test and mail to developer when fail') {
    triggers {
        upstream {
            upstreamProjects('job1-create web deployment')
            threshold('SUCCESS')
        }
    }
    steps {
        shell('bash /task6_code/job2.sh')
    }
}
buildPipelineView('devops_task-6') {
    filterBuildQueue()
    filterExecutors()
    title('Task-6: using groovy code')
    displayedBuilds(5)
    selectedJob('job1-create web deployment')
    alwaysAllowManualTrigger()
    showPipelineParameters()
    refreshFrequency(60)
}
