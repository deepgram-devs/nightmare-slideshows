<script>
export default {
	props: {
		listen: Boolean,
		generate: Boolean,
		done: Boolean
	}
}
</script>

<style scoped>
.status-container {
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	width: 100%;
	/* margin: 20px 0px; */
}
.status {
	color: #aab8ce;
	border-bottom: solid #aab8ce 3px;
	padding: 10px 20px;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	transition-duration: 0.5s;
	transition-property: color, border-bottom-color;
}
.status-active {
	color: black;
	border-bottom-color: #e93d45;
}
</style>

<template>
<footer class="footer fixed-bottom status-container">
	<div class="status status-listen" :class="{ 'status-active': listen }" >
		<h3>Ready to listen...</h3>
	</div>
	<div v-if="generate" class="status status-generate" :class="{ 'status-active': generate }">
		<h3>Generating...</h3>
	</div>
	<div v-if="done" class="status status-done" :class="{ 'status-active': done }">
		<h3>Complete.</h3>
	</div>
</footer>
</template>
