import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-average',
  template: `
    <button (click)="show = !show">{{show ? 'hide' : 'show'}}</button>
    show = {{show}}
    <br>
    <div *ngIf="show; else elseBlock">Text to show</div>
    <ng-template #elseBlock>Alternate text while primary text is hidden</ng-template>
`,
  styleUrls: ['./average.component.css']
})
export class AverageComponent implements OnInit {

    show: boolean = true;
  

  constructor() { }

  ngOnInit(): void {
  }

}
