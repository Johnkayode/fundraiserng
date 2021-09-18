<template>
    <div>
        <div class="form-group">
            <div class="alert mt-2" :class="message.status" role="alert" v-if="message">
                {{ message.text }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Confirm",
}
</script>

<style scoped>

</style>
