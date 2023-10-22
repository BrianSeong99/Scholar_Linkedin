# API Convention

## Main Home Page

```javascript
/**
 * 	@get returns All field nodes and relevant links.
 * 	the response is formatted as follow: 
 *	[
 *		{
 *			time: '', // ex. 2020-03, year and month,
 *			data: {
 *				largestNodeSize: Number, // the largest number of people among all fields across all time.
 *				nodes: [
 *					{
 *						id: '', // id of the node
 *						name: '', // name of the node
 *						_size: Number, // the actual number of all people in this field,
 *						_color: Number, // number of the color set. There will be several color sets available in the frontend, written in css. The amounts of the sets we have will depend on amounts of fields we have. ex, 'Data Mining' will return 1, 'Database' will return 2, etc.
 *					},		
 *				],
 *				links: []
 *			}
 *		}
 *	]
 */
getFields() {
	request(baseurl+'/fields');
}
```

## Field Details Page

```javascript
/**
 * 	@get returns All field nodes and relevant links.
 * 	the response is formatted as follow: 
 *	[
 *		{
 *			time: '', // ex. 2020-03, year and month,
 *			data: {
 *				largestNodeSize: Number, // the largest size number of this field.
 *				nodes: [
 *					{
 *						id: '', // id of the node
 *						name: '', // name of the node
 *						_size: Number, // the influencial rating of the person,
 *            link: '', // http link to the author's aminor profile
 *						info: {
 *							paper: Number,
 *							xxx: xxx,
 *							...... 
 *						}
 *					},		
 *				],
 *				links: [
 *					id: Number,
 *					name: String, // this name is a label for the type of connection of the two nodes, for example "师生关系", "母子关系"
 *					sid: Number,
 *					tid: Number
 *				]
 *			}
 *		}
 *	]
 */
getFieldDetails(query) {
	request(baseurl+'/fields/' + query); // query would look like "fieldname/?limit=100"
}
```


```javascript
response = {
    name: String,
	info: {
		institution: String,
		occupation: String
		summary: String,
		numberOfFollowers: Number,
		interests: [''], // ["Data_Mining", "Web_Mining"]
	},
	papers: [
			{
				id: Number,
				title: String,
				summary: String,
				link: String
				influence: Number
				date: Data()
			},
		
	],
	paperTrend: {
		publish: {
			date: ['2016', '2017', '2018', ....]
			amounts: [Number, Number, .....]
		},
		citation: {
			date: ['2016', '2017', '2018', ....]
			amounts: [Number, Number, .....]
		},
	},
	personalGraph: {
		nodes: [
			{
				id: Number,
				name: String,
				field: String,
				link: '' // http link to the author's aminor profile
			},
			links: [
				{
					id: Number,
					name: String, // this should be the field
					sid: Number,
					tid: Number
				}
			]
		]
	},
	communityGraph: {
		nodes: [
			{
				id: Number,
				name: String,
				community: String,
				link: '', // http link to the author's aminor profile
			}
		],
		links: [
			{
				id: Number,
				name: String, // name here should be the community
				sid: Number,
				tid: Number
			}
		]
	}

}
getPersonDetails(query) {
	request(baseurl + '/person/' + query) // query like "?name=john_smith"
}
```

## News
```javascript
/**
 * 	@get returns news of a specific topic, person, field, etc
 * 	the response is formatted as follow: 
 *	[
 *		{
 *			id: Number,
 *			title: String,
 *			date: String, // better follow the javascript Date() format
 *			url: String, // content source website link
 *			fields: [''], // list of field tags
 *			img: Object, // if there is one
 *			content: String
 *		}
 *	]
 */
getNews(query) {
	request(baseurl+'/news/' + query); 
	/** query is the name of the author or field for now. 
	 * the name will be connected with underscore. 
	 * ex: John Smith -> John_Smith
	 * query = ?person=John_Smith&field=Data_Mining
	 * query = ?person=John_Smith
	 * query = ?field=Data_Mining
	 */
}
```
