const progressBar = document.getElementsByClassName('progress-bar')[0]
setInterval(()=>{
	const computedStyle = getComputedStyle(progressBar)
	const width = parseFloat(computedStyle.getPropertyValue('--width')) || 0
	progressBar.style.setProperty('--width', width+ 0.1) // what if i do if link is clicked on, width + 20
}, 5)
