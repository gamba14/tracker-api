import { Component, OnInit } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

@Component({
  selector: 'requester',
  template:`
            <p>{{results}}</p>
  `
})
  export class aplink implements OnInit {

  results: string[];

  // Inject HttpClient into your component or service.
  constructor(private http: localhost:5000) {}

  ngOnInit(): void {
    // Make the HTTP request:
    this.http.get('/v1.0/parcels').subscribe(data => {
      // Read the result field from the JSON response.
      this.results = data['results'];
    });
  }
}
