<script setup>
import StatusFooter from './components/StatusFooter.vue';
import AudioUploader from './components/AudioUploader.vue';
</script>

<template>
<main>
  <div class="container col-xl-10 col-xxl-8 px-4 py-5 app-container center-me">
      <h1 class="display-4 fw-bold lh-1 mb-3">Looking for some ✨ video magic?</h1>
	  <img class="alf" src="/static/alf.png" />
    <div class="row py-4">
      <div class="col">
        <h2 class="">Build custom slideshows, perfectly matched to your audio.</h2>
        <p class="copy fs-4">Jazz up your stories with artisinally crafted neural net imagery. Upload an audio file and we'll produce a custom video for it.</p>
      </div>
    </div>
	<div class="row">
		<div class="col-xl-10 col-xxl-8 px-4 py-5 upload-form">
			<form class="p-4 p-md-5 border bg-dark">
			<div class="left">
				<label class="mb-1" for="floatingInput">Pick an audio file:</label>
				<input type="file" accept="audio/*" class="form-control" v-on:change="handleChange"/>
				<i class="mt-3 aside">We accept over 40 common audio file formats including MP3, WAV, FLAC, M4A, and more.</i>
			</div>
			<button class="mt-4 btn btn-lg btn-primary" type="submit" v-on:click="submitFile()">Create My Slideshow</button>
			</form>
		</div>
	</div>
	<AudioUploader @transcribe="handleTranscribe" @listen="handleListen" @summarize="handleSummarize" @done="handleDone"/>
  </div>

	<StatusFooter :listen="listen" :generate="generate" :done="done" />
</main>
</template>