# FFT完整算法

## Intro

**站在巨人的肩膀上写bug**

## Example

```shell
@"Input Sequence : Sequence is : 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \r\n"
@"FFT Sequence : Sequence is : 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \r\n"
```

## Code

```c
//站在巨人的肩膀上
#include <stdio.h>
#include <math.h>

#define PI 3.1415926
#define SAMPLENUMBER 128

void InitForFFT();
void InputWave();
void FFT(float dataR[], float dataI[]);
void PrintSequence(int seq[]);

int INPUT[SAMPLENUMBER], DATA[SAMPLENUMBER];
float fWaveR[SAMPLENUMBER], fWaveI[SAMPLENUMBER], w[SAMPLENUMBER];
float sin_tab[SAMPLENUMBER], cos_tab[SAMPLENUMBER];

int main()
{
	int i;

	InitForFFT(); //采样
	InputWave();
	for (i = 0; i < SAMPLENUMBER; i++)
	{
		fWaveR[i] = INPUT[i];
		fWaveI[i] = 0.0f;
		w[i] = 0.0f;
	}
	FFT(fWaveR, fWaveI);
	for (i = 0; i < SAMPLENUMBER; i++)
	{
		DATA[i] = w[i];
	}
	printf("FFT Sequence : ");
	PrintSequence(DATA);
	return 0;
}

void FFT(float dataR[], float dataI[])
{
	int x0, x1, x2, x3, x4, x5, x6, xx;
	int i, j, k, b, p, L;
	float TR, TI, temp;
	int bit_len = ceil(log2(SAMPLENUMBER));
	//求逆序数
	for (i = 0; i < SAMPLENUMBER; i++)
	{

		int reverse_seq = 0;
		for (int bit = 0; bit < bit_len; bit++)
		{
			dataI[0] = dataR[0];
			if (bit > 0)
				reverse_seq += ((i / (int)pow(2, bit)) & 0x01) * pow(2, bit_len - bit - 1);
			else
				reverse_seq += (i & 0x01) * pow(2, bit_len - 1);
		}
		dataI[reverse_seq] = dataR[i];
	}

	for (i = 0; i < SAMPLENUMBER; i++)
	{
		dataR[i] = dataI[i];
		dataI[i] = 0;
	}

	//FFT操作
	for (L = 1; L <= bit_len; L++)
	{ /* for(1) */
		b = 1;
		i = L - 1;
		while (i > 0)
		{
			b = b * 2;
			i--;
		}							 /* b= 2^(L-1) */
		for (j = 0; j <= b - 1; j++) /* for (2) */
		{
			p = 1;
			i = 7 - L;
			while (i > 0) /* p=pow(2,7-L)*j; */
			{
				p = p * 2;
				i--;
			}
			p = p * j;
			for (k = j; k < 128; k = k + 2 * b) /* for (3) */
			{
				TR = dataR[k];
				TI = dataI[k];
				temp = dataR[k + b];
				dataR[k] = dataR[k] + dataR[k + b] * cos_tab[p] + dataI[k + b] * sin_tab[p];
				dataI[k] = dataI[k] - dataR[k + b] * sin_tab[p] + dataI[k + b] * cos_tab[p];
				dataR[k + b] = TR - dataR[k + b] * cos_tab[p] - dataI[k + b] * sin_tab[p];
				dataI[k + b] = TI + temp * sin_tab[p] - dataI[k + b] * cos_tab[p];
			} /* END for (3) */
		}	  /* END for (2) */
	}		  /* END for (1) */
	for (i = 0; i < SAMPLENUMBER / 2; i++)
	{
		w[i] = sqrt(dataR[i] * dataR[i] + dataI[i] * dataI[i]);
	}
} /* END FFT */

void InitForFFT()
{
	int i;

	for (i = 0; i < SAMPLENUMBER; i++)
	{
		sin_tab[i] = sin(PI * 2 * i / SAMPLENUMBER);
		cos_tab[i] = cos(PI * 2 * i / SAMPLENUMBER);
	}
}

void InputWave()
{
	int i;

	for (i = 0; i < SAMPLENUMBER; i++)
	{
		INPUT[i] = 1; //输入波形
	}
	printf("Input Sequence : ");
	PrintSequence(INPUT);
}

void PrintSequence(int seq[])
{
	int i;
	for (i = 0; i < SAMPLENUMBER; i++)
	{
		printf("%d, ", seq[i]);
	}
	printf("\n");
}

```

