function buttonFunction() {
	odie = document.getElementById("sa1").value;
	aussie = document.getElementById("sa2").value;
	score = 0
	if (odie == "Odie") {
		score = score + 1
	}
	if (aussie == "Canberra") {
	score = score + 1
	}
	if ((document.getElementById("q1a1").checked) && (document.getElementById("q1a2").checked)) {
		score = score + 1;
	}
	if ((document.getElementById("q1a1").checked) && (document.getElementById("q1a2").checked) && (document.getElementById("q1a3").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q1a1").checked) && (document.getElementById("q1a2").checked) && (document.getElementById("q1a4").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q1a1").checked) && (document.getElementById("q1a2").checked) && (document.getElementById("q1a3").checked) && (document.getElementById("q1a4").checked)) {
		score = score + 1;
	}
	if ((document.getElementById("q2a1").checked) && (document.getElementById("q2a3").checked) && (document.getElementById("q2a4").checked)) {
		score = score + 1;
	}
	if ((document.getElementById("q2a1").checked) && (document.getElementById("q2a2").checked) && (document.getElementById("q2a3").checked) && (document.getElementById("q2a4").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q2a1").checked) && (document.getElementById("q2a2").checked)) {
		score = score + 0;
	}
	if (document.getElementById("q3a4").checked) {
		score = score + 1;
	}
	if ((document.getElementById("q3a4").checked) && (document.getElementById("q3a1").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q3a4").checked) && (document.getElementById("q3a2").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q3a4").checked) && (document.getElementById("q3a3").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q3a4").checked) && (document.getElementById("q3a1").checked) && (document.getElementById("q3a2").checked) && (document.getElementById("q3a3").checked)) {
		score = score + 2;
	}
	if ((document.getElementById("q4a1").checked) && (document.getElementById("q4a4").checked)) {
		score = score + 1;
	}
	if ((document.getElementById("q4a4").checked) && (document.getElementById("q4a1").checked) && (document.getElementById("q4a2").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q4a4").checked) && (document.getElementById("q4a1").checked) && (document.getElementById("q4a3").checked)) {
		score = score - 1;
	}
	if ((document.getElementById("q4a4").checked) && (document.getElementById("q4a1").checked) && (document.getElementById("q4a2").checked) && (document.getElementById("q4a3").checked)) {
		score = score + 1;
	}
	if (document.getElementById("q1yes").checked) {
		score = score + 1;
	}
	if (document.getElementById("q2no").checked) {
		score = score + 1;
	}
	if (document.getElementById("q3no").checked) {
		score = score + 1;
	}
	if (document.getElementById("q4yes").checked) {
		score = score + 1;
	}
	document.write(" ")
	if (10 > score > 4) {
		document.write("Congratulations, you passed with a score of " + (score * 10) + " %");
	}
	if (score < 5) {
		document.write("Sorry, you failed with a score of " + (score * 10) + " %. ");
	}
	if (score == 10) {
		document.write("Congratulations, your got a perfect score of 100%!");
	}
	if (score < 10) {
		document.write("The strawberry may be considered a berry, but berries are considered fruit, so 'Stawberry' and 'Apple' were the answers to question 1. Brown was the color not present in a rainbow, so Red, Green, and Orange were the correct answers to question 2. Snoopy was the name of Charlie Brown's mischevious and often misbehaving beagle, and the numbers less than 4 are 3 and -2. The CN tower is still the tallest building in Canada, but Nemo is not a pufferfish. He is a clownfish, a species known for its incredibly low intelligence and cannibalism. Coffee is made from the seeds of a cherry-like fruit, and since fruit and berries are one in the same, coffee is made from a berry. The name of the dog in 'Garfield' was 'Odie', known for having more tongue than brains, and being kicked off a countertop by an obese cat. And finally, the capital of Australia is Canberra, which sounds similar to Kookaburra, a loud, annoying bird and probably the only thing not overly dangerous in Australia. Thanks for taking the quiz, hope you enjoyed!"); 
	}
}