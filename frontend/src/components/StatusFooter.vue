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

/**
 * ==============================================
 * Dot Elastic
 * ==============================================
 */
.dot-elastic {
  position: relative;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #9880ff;
  color: #9880ff;
  animation: dotElastic 1s infinite linear;
}

.dot-elastic::before, .dot-elastic::after {
  content: '';
  display: inline-block;
  position: absolute;
  top: 0;
}

.dot-elastic::before {
  left: -15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #9880ff;
  color: #9880ff;
  animation: dotElasticBefore 1s infinite linear;
}

.dot-elastic::after {
  left: 15px;
  width: 10px;
  height: 10px;
  border-radius: 5px;
  background-color: #9880ff;
  color: #9880ff;
  animation: dotElasticAfter 1s infinite linear;
}

@keyframes dotElasticBefore {
  0% {
    transform: scale(1, 1);
  }
  25% {
    transform: scale(1, 1.5);
  }
  50% {
    transform: scale(1, 0.67);
  }
  75% {
    transform: scale(1, 1);
  }
  100% {
    transform: scale(1, 1);
  }
}

@keyframes dotElastic {
  0% {
    transform: scale(1, 1);
  }
  25% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1, 1.5);
  }
  75% {
    transform: scale(1, 1);
  }
  100% {
    transform: scale(1, 1);
  }
}

@keyframes dotElasticAfter {
  0% {
    transform: scale(1, 1);
  }
  25% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1, 0.67);
  }
  75% {
    transform: scale(1, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
</style>

<template>
<footer class="footer fixed-bottom status-container">
	<div class="status status-listen">
		<h3 v-if="listen">Ready to listen...</h3>
		<h3 v-if="generate">Generating (hang tight!)ㅤ</h3>
		<div v-if="generate" class="snippet" data-title=".dot-elastic">
			<div class="stage">
				<div class="dot-elastic"></div>
			</div>
		</div>
		<h3 v-if="done">Complete.</h3>
	</div>
	<!-- <div v-if="generate" class="status status-generate" :class="{ 'status-active': generate }">
	</div>
	<div v-if="done" class="status status-done" :class="{ 'status-active': done }">
	</div> -->
</footer>
</template>
