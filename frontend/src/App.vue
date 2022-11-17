<script setup>
import StatusFooter from './components/StatusFooter.vue';
</script>

<script>
import axios from 'axios';
import { handleError } from './utils/error.js';

export const SERVER_URL = `http://127.0.0.1:8000/`

export default {
	data() {
		return {
			listening: true,
			generating: false,
			finished: false,
			videoPath: null
		}
	},
	computed: {
		listen() {
			return this.listening;
		},
		generate() {
			return this.generating;
		},
		done() {
			return this.finished;
		},
		getVideoResults() {
			return this.videoPath;
		}
	},
	methods: {
		onSubmit(e) {
			console.log('submitting')
			e.preventDefault();
			this.listening = false;
			this.generating = true;
			const file = document.getElementById('audio-file').files[0];
			axios({
				method: `POST`,
				url: SERVER_URL,
				data: file
			}).then(response => {
				if(response.status == 200) {
					console.log(response);
					const videoPath = response.data.path;
					this.videoPath = videoPath;
					this.generating = false;
					this.finished = true;
					console.log(this.videoPath);
				} else {
					this.listening = true;
					this.generating = false;
					handleError('There was an error transcibing the audio file uploaded. Check the log for more details.', response);
				}
			}).catch(error => {
				this.listening = true;
				this.generating = false;
				handleError('There was an error transcribing the audio file uploaded. Check the log for more details.', error);
			});
		},
	}
}
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
			<form v-on:submit="onSubmit" class="p-4 p-md-5 border bg-dark">
			<div class="left">
				<label class="mb-1" for="floatingInput">Pick an audio file:</label>
				<input id="audio-file" type="file" accept="audio/*" class="form-control" />
				<i class="mt-3 aside">We accept over 40 common audio file formats including MP3, WAV, FLAC, M4A, and more.</i>
			</div>
			<button class="mt-4 btn btn-lg btn-primary" type="submit">Create My Slideshow</button>
			</form>
		</div>
	<div v-if="done">
		<hr />
		<video controls>
			<source :src="SERVER_URL + this.videoPath" type="video/mp4"/>
		</video>
	</div>
	</div>

  </div>

	<StatusFooter :listen="listen" :generate="generate" :done="done" />
</main>
</template>