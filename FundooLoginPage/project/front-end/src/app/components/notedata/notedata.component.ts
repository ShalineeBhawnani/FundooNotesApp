import { Component, OnInit } from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material";

@Component({
  selector: 'app-notedata',
  templateUrl: './notedata.component.html',
  styleUrls: ['./notedata.component.scss']
})
export class NotedataComponent implements OnInit {
  description:string;


  constructor() { }

  ngOnInit() {
  }

}
