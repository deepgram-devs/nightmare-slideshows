<script>
import axios from 'axios';
import { handleError } from '../utils/error.js';

export default {
	methods: {
		handleYoutubeSummary(e) {
			this.$emit('listen');
			setTimeout(() => {
				this.$emit('summarize');
			}, 1500);
			const youtubeURL = document.getElementById('youtube-url').value;
			axios.post('https://onk7ysrjnb.execute-api.us-east-1.amazonaws.com/Production/youtube', {
				'video_url': youtubeURL
			}, { 'Content-Type': 'application/json' }).then(response => {
				if(response.status == 200) {
					console.log(response);
					const doneData = {
						'summary': response.data.summary,
						'videoTitle': response.data.video_title,
						'videoThumbnail': response.data.video_thumbnail
					};
					this.$emit('done', doneData);
				} else {
					handleError('There was an error while processing the video. Check the log for more details.', response);
				}
			}).catch(error => {
				handleError('There was an error while processing the video. Check the log for more details.', error);
			});
		},
		handleChange(e) {
			this.$emit('listen');
			const file = document.getElementById('upload-button').files[0];
			axios({
				method: 'POST',
				url: 'https://api.deepgram.com/v1/listen',
				headers: {
					'content-type': file.type,
					'Authorization': `Token ${localStorage.getItem('DG_API_KEY')}`
				},
				params: {
					language: 'en-US',
					punctuate: true,
					profanity_filter: false,
					diarize: false,
					multichannel: false,
					numeral: true,
					utterances: false
				},
				data: file
			}).then(response => {
				if(response.status == 200) {
					const transcript = response.data.results.channels[0].alternatives[0].transcript;
					this.handleSummary(transcript);
					this.$emit('transcribe', transcript);
					console.log(response);
				} else {
					handleError('There was an error transcibing the audio file uploaded. Check the log for more details.', response);
				}
			}).catch(error => {
				handleError('There was an error transcribing the audio file uploaded. Check the log for more details.', error);
			});
		},
		handleSummary(transcript) {
			this.$emit('summarize');
			axios({
				method: 'POST',
				url: 'https://app.thetextapi.com/text/summarize',
				headers: {
					'apikey': localStorage.getItem('TA_API_KEY'),
					'Content-Type': 'application/json'
				},
				data: {
					text: transcript
				}
			}).then(response => {
				if(response.status == 200) {
					const summary = response.data.summary;
					this.$emit('done', { summary });
					console.log(response);
				} else {
					handleError('There was an error summarizing the text. Check the log for more details.', response);
				}
			}).catch(error => {
				handleError('There was an error summarizing the text. Check the log for more details.', error);
			});
		}
	}
}
</script>

<style scoped>
.uploader-container {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	width: 100%;
}
#upload-button {
	border: 0;
  	clip: rect(0, 0, 0, 0);
  	height: 1px;
  	overflow: hidden;
  	padding: 0;
 	position: absolute !important;
 	white-space: nowrap;
 	width: 1px;
}
.button {
	margin: 0px 10px;
	padding: 5px 25px;
	border: none;
	cursor: pointer;
	text-transform: uppercase;
	font-weight: bold;
	transition-duration: .5s;
	transition-property: color, background-color, border;
	color: white;
	background-color: #e93d45;
}
.button:hover {
	color: #e93d45;
	background-color: white;
}
.upload-option-text {
	font-weight: bold;
	text-transform: uppercase;
	display: block;
}
.youtube-uploader {
	font-size: 16px;
}
#youtube-url {
	border: 1px solid black;
	font-size: 25px;
}
</style>

<template>
<div class="uploader-container">
	<input type="file" accept="audio/*" id="upload-button" v-on:change="handleChange"/>
	<label for="upload-button" class="button">Upload an Audio File</label>
</div>
</template>