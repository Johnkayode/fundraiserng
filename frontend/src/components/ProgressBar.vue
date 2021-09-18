<template>
    <div class="progress mt-3" >
        <div class="progress-bar" role="progressbar"   :style="{width: percentage + '%'}" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</template>

<script>
 
    export default {
        props: ['percentage'],
    }
</script>


<style scoped>
    .progress{
        height: 5px;
    }
    .progress-bar{
        background: green;
    }
</style>