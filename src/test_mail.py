test_mail1 = """Return-Path: <test.test@gmail.com>
Received: from mail-lj1-f171.google.com (mail-lj1-f171.google.com [209.85.208.171])
 by inbound-smtp.eu-west-1.amazonaws.com with SMTP id i4ohgmt4h3pr2vpnuglpvtmq4v37mh3rhp9c5v01
 for test@realestate-tracker.com;
 Wed, 29 Jun 2022 19:34:08 +0000 (UTC)
Received-SPF: pass (spfCheck: domain of _spf.google.com designates 209.85.208.171 as permitted sender) client-ip=209.85.208.171; envelope-from=test.test@gmail.com; helo=mail-lj1-f171.google.com;
Authentication-Results: amazonses.com;
 spf=pass (spfCheck: domain of _spf.google.com designates 209.85.208.171 as permitted sender) client-ip=209.85.208.171; envelope-from=test.test@gmail.com; helo=mail-lj1-f171.google.com;
 dkim=pass header.i=@gmail.com;
 dmarc=pass header.from=gmail.com;
X-SES-RECEIPT: AEFBQUFBQUFBQUFIc0NoZTFvanpCZkIxTFNSUmU2elRTM2E2czYxWlZaVW1SZklLM0lqY2kwOW0xdGhXdE9IOXRFMWt1RVNGdUJPYUJ1bWxKMWFqWnA0eDVuUHBTeEpvS0M3SEF0NlFZSjIxQlJpWnVQdTVJR1U1dENBSWFXUkpUR0FlQWZYMVhqSm5lS24rU3lOV2VnVzFPZkhiUXZyb2w3ME93ZERIREpEYXkyK01kS1YwblNrS29KMUNyOHJSZ2xLdllJeHJFYkVWNlMrc3VucUZkVmFpUjVvdTBOUTBEUWNkMTBsYm1acW1VUndxbDRTRnptbXRyR1RtSk9kdnkyaHVtMG0yQlN6ZFVCa01qWkJtU2RFMklPdTUxeVZzL2VqZUpXbUVBZjlVZGFvMkFtVU9wdXpIbmFObllEamYvY1liRVdra3lBNUE9
X-SES-DKIM-SIGNATURE: a=rsa-sha256; q=dns/txt; b=CXNIJ+X/mWBENKiEBsCiXhvftvPOpDxHeD+SjX8s1HZxqFg5f3ALImToL0J9lbzs9CQ4lJryZ7yRsvO7ePv19+WkcvtYHLGPWeyZ1rJmQzdzZsBxz+TUYektpkblUnGzCXZ8lUtK6zOSFDxwDOeF47ePn/193PbWx5V/VCsvdDI=; c=relaxed/simple; s=ihchhvubuqgjsxyuhssfvqohv7z3u4hn; d=amazonses.com; t=1656531248; v=1; bh=sX7ysj5g3+rM1JTpQfk+AAkaBETX/sYnuorqHVc2BNM=; h=From:To:Cc:Bcc:Subject:Date:Message-ID:MIME-Version:Content-Type:X-SES-RECEIPT;
Received: by mail-lj1-f171.google.com with SMTP id s10so20204722ljh.12
        for <test@realestate-tracker.com>; Wed, 29 Jun 2022 12:34:08 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20210112;
        h=mime-version:references:in-reply-to:from:date:message-id:subject:to;
        bh=E+TP2uHNgZ4xtjaG6eyfIVPdonDXePTv3a7mjArm2TY=;
        b=SroOwAWep9H0Rfp3xYdG3Vxz0FQgd5yksbwLrLeaBMkgA4uI+2cbdtwjtmsRVXz8j3
         fg0kBUsKnL58cExStFA7zaDml+5etv2GPEUXpoUx5Z6Ktki3gu+9bKXI74FCpgsh1n1c
         odXh/a8JChdPBi/3QTTsU8oCS08/ekZAMpOX6X3ySdXuFHG3sWQUAZx1Vu6b02DME0vB
         p23VnbbECJwYuKKnoSzBW4bLJ5owxG2VVF9g4ijJUCgn83OOFJ1Pn8H2RQNt7ZKDJsxu
         D80ueH04hY1ionroSVQaLqWes3rG3pWNxy4lpjvZkCSBKsYqWkJ0Rf+9dtBwKZ19KWdt
         wlzQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20210112;
        h=x-gm-message-state:mime-version:references:in-reply-to:from:date
         :message-id:subject:to;
        bh=E+TP2uHNgZ4xtjaG6eyfIVPdonDXePTv3a7mjArm2TY=;
        b=Ow90Sia9Zd27Wp5eUAEKViRT0dYMJo/o9s5hmckx5fYZXAV75sdxtdK/rvuLuR/kEA
         RMYN1TjljhWJz7o9WSjBca2UN+FZU45f0tf1ws5F385fmAZIx3USRugSG9VMiBsr7VuM
         2qiaoKOYeio3ax+/Ld1c8eb4m8xl9oBkZ8zl4xouyFzYTQ0bCmsrg9KdvJRCh8QgPeW5
         zncw8q+5ApubpHRVium7OY6aUUP4cx+pFw5a1LtIxsz3/trsNPurLFHP80PPVpJedbB6
         uqZB2mfZ0LfS8WtcFq8vCXt2rSP/pu8pkKVjjs6BzZQHz0TvJEfUKsBlchoyt1JTRc9N
         VgMA==
X-Gm-Message-State: AJIora9n+xTRYge6cJPxzFJRZ1JssSl+oDTZjAn6KvqF+UJS9z1ytlFl
	CXt7Vg0/3ErouFHCUs5CSNgRe8HHyncBHxpUgiYQ+2Zu
X-Google-Smtp-Source: AGRyM1u2+BxCkh8U3p3prLhEV4vW8rdzZLhPGRblx5ssANI26SgqnMoeKARaEJuN/b++nwf/bsMXnPYBzigDLwkabs4=
X-Received: by 2002:a2e:b8d6:0:b0:25a:99ce:5c32 with SMTP id
 s22-20020a2eb8d6000000b0025a99ce5c32mr2750974ljp.95.1656531246993; Wed, 29
 Jun 2022 12:34:06 -0700 (PDT)
MIME-Version: 1.0
References: <01020181b06518db-931334a5-a8bd-422c-b3ef-e7bfc52eaf6c-000000@eu-west-1.amazonses.com>
In-Reply-To: <01020181b06518db-931334a5-a8bd-422c-b3ef-e7bfc52eaf6c-000000@eu-west-1.amazonses.com>
From: test test <test.test@gmail.com>
Date: Wed, 29 Jun 2022 22:33:55 +0300
Message-ID: <CAFhABNEfXwB0SGwk4C=Xk0DrrrZqT5VcxhQ8wnP4sUKnbrjgZg@mail.gmail.com>
Subject: =?UTF-8?B?RndkOiDXnteV15PXoteV16og15fXk9ep15XXqiDXqdei15zXlSDXkdeQ16rXqCDXmdeTMg==?=
To: test@realestate-tracker.com
Content-Type: multipart/alternative; boundary="0000000000008956e605e29b3c5b"

--0000000000008956e605e29b3c5b
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: base64

LS0tLS0tLS0tLSBGb3J3YXJkZWQgbWVzc2FnZSAtLS0tLS0tLS0NCkZyb206IFlhZDIgPGluZm9A
eWFkMi5jby5pbD4NCkRhdGU6IFdlZCwgMjkgSnVuIDIwMjIgYXQgMTk6NTcNCuKAqlN1YmplY3Q6
INee15XXk9ei15XXqiDXl9eT16nXldeqINep16LXnNeVINeR15DXqteoINeZ15My4oCsDQpUbzog
PGFsb24uc3Rlcm4yMDZAZ21haWwuY29tPg0KDQoNCtee15XXk9ei15XXqiDXl9eT16nXldeqINep
16LXnNeVINei15HXldeoDQrXl9eT16jXmdedOiAzIC0gNSB8INee15fXmdeoOiAxLDAwMCwwMDAg
LSA0LDAwMCwwMDAgfA0KIOKAjCDigIwg4oCMICDigIwg4oCMIOKAjCAg4oCMIOKAjCDigIwgIOKA
jCDigIwg4oCMICDigIwg4oCMIOKAjCAg4oCMIOKAjCDigIwgIOKAjCDigIwg4oCMICDigIwg4oCM
IOKAjCAg4oCMIOKAjCDigIwgIOKAjCDigIwg4oCMDQog4oCMIOKAjCDigIwgIOKAjCDigIwg4oCM
ICDigIwg4oCMIOKAjCAg4oCMIOKAjCDigIwNCg0K15DXnSDXkNeZ16DXmiDXqNeV15DXlCDXnteZ
15nXnCDXlteUINeb16jXkNeV15kg15zXl9elINeb15DXnw0KPGh0dHBzOi8veTItbm90aWZpY2F0
aW9uLXNlcnZpY2UuczMtZXUtd2VzdC0xLmFtYXpvbmF3cy5jb20vbWFpbHMvbXktYWxlcnRzLzZf
MjlfMjAyMi8yMDMzNjcxNTE0NzUyLjg3NjctODVjZWNhZTg3YTdiYWFhNjY0Nzg2MTI4ZTYwZTNh
YmUuaHRtbD4NCltpbWFnZTogWWFkMiBDYXRlZ29yeSBCYW5uZXJdDQo8aHR0cHM6Ly93d3cueWFk
Mi5jby5pbD91dG1fc291cmNlPW15QWxlcnRzUmVhbGVzdGF0ZSZ1dG1fbWVkaXVtPWVtYWlsJnV0
bV9jYW1wYWlnbj1Mb2dvPg0KDQoqINeU15nXmSDXkNec15XXnywgKg0KDQrXntem15DXoNeVIDEw
NiDXnteV15PXoteV16og15fXk9ep15XXqiDXqdee16rXkNeZ157XldeqINec15fXmdek15XXqSDX
qdec15o6DQoNCirXk9eZ16jXldeqINec157Xm9eZ16jXlCDXkdee16jXm9eWKg0KDQrXl9eT16jX
mdedOiAzIC0gNSB8INee15fXmdeoOiAxLDAwMCwwMDAgLSA0LDAwMCwwMDAgfA0KPGh0dHBzOi8v
d3d3LnlhZDIuY28uaWwvaXRlbS92amVneWprOT90b3BBcmVhPTImcm9vbXM9My01JnByaWNlPTEw
MDAwMDAtNDAwMDAwMCZjYXRlZ29yeT1yZWFsZXN0YXRlJnN1YkNhdGVnb3J5PWZvcnNhbGUmaXNG
cm9tTXlBbGVydHM9dHJ1ZSZteUFsZXJ0c1NvcnQ9MSZ1dG1fc291cmNlPW15QWxlcnRzUmVhbGVz
dGF0ZSZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1teUFsZXJ0c0FkPg0KDQoq4oCPMiwy
NTAsMDAwIOKCqioNCteS150g15HXmNeo15nXmdeTINeQ15nXnw0KDQrXodei15PXmdeUINeS15DX
ldefIDYNCg0K15LXqNeZ158g15XXotedIHwg15PXmdeo15QgfCA0INeX15PXqNeZ150gfCA4MCDX
nte016gNCg0K15zXpNeo15jXmdedINeg15XXodek15nXnQ0KPGh0dHBzOi8vd3d3LnlhZDIuY28u
aWwvaXRlbS92amVneWprOT90b3BBcmVhPTImcm9vbXM9My01JnByaWNlPTEwMDAwMDAtNDAwMDAw
MCZjYXRlZ29yeT1yZWFsZXN0YXRlJnN1YkNhdGVnb3J5PWZvcnNhbGUmaXNGcm9tTXlBbGVydHM9
dHJ1ZSZteUFsZXJ0c1NvcnQ9MSZ1dG1fc291cmNlPW15QWxlcnRzUmVhbGVzdGF0ZSZ1dG1fbWVk
aXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1teUFsZXJ0c0FkPg0KDQo8aHR0cHM6Ly93d3cueWFkMi5j
by5pbC9pdGVtL2ZjNGdnZm1xP3RvcEFyZWE9MiZyb29tcz0zLTUmcHJpY2U9MTAwMDAwMC00MDAw
MDAwJmNhdGVnb3J5PXJlYWxlc3RhdGUmc3ViQ2F0ZWdvcnk9Zm9yc2FsZSZpc0Zyb21NeUFsZXJ0
cz10cnVlJm15QWxlcnRzU29ydD0xJnV0bV9zb3VyY2U9bXlBbGVydHNSZWFsZXN0YXRlJnV0bV9t
ZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPW15QWxlcnRzQWQ+DQoNCirigI8yLDM1MCwwMDAg4oKq
Kg0K15LXnSDXkdeY16jXmdeZ15Mg15DXmdefDQoNCtem15nXqNec16HXldefIDIyDQoNCteq16fX
ldee15QgLyDXp9eo15nXqiDXl9eW16DXmSB8INeS15Iv16TXoNeY15TXkNeV15YgfCA1INeX15PX
qNeZ150gfCAxNjAg157XtNeoDQoNCtec16TXqNeY15nXnSDXoNeV16HXpNeZ150NCjxodHRwczov
L3d3dy55YWQyLmNvLmlsL2l0ZW0vZmM0Z2dmbXE/dG9wQXJlYT0yJnJvb21zPTMtNSZwcmljZT0x
MDAwMDAwLTQwMDAwMDAmY2F0ZWdvcnk9cmVhbGVzdGF0ZSZzdWJDYXRlZ29yeT1mb3JzYWxlJmlz
RnJvbU15QWxlcnRzPXRydWUmbXlBbGVydHNTb3J0PTEmdXRtX3NvdXJjZT1teUFsZXJ0c1JlYWxl
c3RhdGUmdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249bXlBbGVydHNBZD4NCg0KPGh0dHBz
Oi8vd3d3LnlhZDIuY28uaWwvaXRlbS83ZGt3YTI4OD90b3BBcmVhPTImcm9vbXM9My01JnByaWNl
PTEwMDAwMDAtNDAwMDAwMCZjYXRlZ29yeT1yZWFsZXN0YXRlJnN1YkNhdGVnb3J5PWZvcnNhbGUm
aXNGcm9tTXlBbGVydHM9dHJ1ZSZteUFsZXJ0c1NvcnQ9MSZ1dG1fc291cmNlPW15QWxlcnRzUmVh
bGVzdGF0ZSZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1teUFsZXJ0c0FkPg0KDQoq4oCP
MSw2OTAsMDAwIOKCqioNCteS150g15HXmNeo15nXmdeTINeQ15nXnw0KDQrXlNeX16nXnteV16DX
kNeZ150NCg0K15zXkSDXlNei15nXqCB8INeT15nXqNeUIHwgMyDXl9eT16jXmdedIHwgNTcg157X
tNeoDQoNCtec16TXqNeY15nXnSDXoNeV16HXpNeZ150NCjxodHRwczovL3d3dy55YWQyLmNvLmls
L2l0ZW0vN2Rrd2EyODg/dG9wQXJlYT0yJnJvb21zPTMtNSZwcmljZT0xMDAwMDAwLTQwMDAwMDAm
Y2F0ZWdvcnk9cmVhbGVzdGF0ZSZzdWJDYXRlZ29yeT1mb3JzYWxlJmlzRnJvbU15QWxlcnRzPXRy
dWUmbXlBbGVydHNTb3J0PTEmdXRtX3NvdXJjZT1teUFsZXJ0c1JlYWxlc3RhdGUmdXRtX21lZGl1
bT1lbWFpbCZ1dG1fY2FtcGFpZ249bXlBbGVydHNBZD4NCg0K15bXnteZ16gg16DXk9ecItefDQo8
aHR0cHM6Ly93d3cueWFkMi5jby5pbC9pdGVtL3puMnNxZTRxP3RvcEFyZWE9MiZyb29tcz0zLTUm
cHJpY2U9MTAwMDAwMC00MDAwMDAwJmNhdGVnb3J5PXJlYWxlc3RhdGUmc3ViQ2F0ZWdvcnk9Zm9y
c2FsZSZpc0Zyb21NeUFsZXJ0cz10cnVlJm15QWxlcnRzU29ydD0xJnV0bV9zb3VyY2U9bXlBbGVy
dHNSZWFsZXN0YXRlJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPW15QWxlcnRzQWQ+DQoN
CirigI8yLDMwMCwwMDAg4oKqKg0K15LXnSDXkdeY16jXmdeZ15Mg15DXmdefDQoNCteZ16nXqNeQ
15wg157XqNeZ15Yn15nXnw0KDQrXpteU15zXldefLCDXqdeZ15vXldeg15kg15fXodeb15XXnyB8
INeT15nXqNeUIHwgMyDXl9eT16jXmdedIHwgODQg157XtNeoDQoNCtec16TXqNeY15nXnSDXoNeV
16HXpNeZ150NCjxodHRwczovL3d3dy55YWQyLmNvLmlsL2l0ZW0vem4yc3FlNHE/dG9wQXJlYT0y
JnJvb21zPTMtNSZwcmljZT0xMDAwMDAwLTQwMDAwMDAmY2F0ZWdvcnk9cmVhbGVzdGF0ZSZzdWJD
YXRlZ29yeT1mb3JzYWxlJmlzRnJvbU15QWxlcnRzPXRydWUmbXlBbGVydHNTb3J0PTEmdXRtX3Nv
dXJjZT1teUFsZXJ0c1JlYWxlc3RhdGUmdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249bXlB
bGVydHNBZD4NCg0K15PXoNeZ15QgLSBVUkJBTklYDQrXnNeb15wg15TXnteV15PXoteV16oNCjxo
dHRwczovL3d3dy55YWQyLmNvLmlsL3JlYWxlc3RhdGUvZm9yc2FsZT90b3BBcmVhPTImcm9vbXM9
My01JnByaWNlPTEwMDAwMDAtNDAwMDAwMCZzdGFydERhdGU9MTY1NjQzNTQyNDIzNi0xNjU2NTIx
ODI0MjM2Jm15QWxlcnRzU29ydD0xJnV0bV9zb3VyY2U9bXlBbGVydHNSZWFsZXN0YXRlJnV0bV9t
ZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPW15QWxlcnRzRmVlZD4NCg0K15zXkCDXqNeV16bXlCDX
nNen15HXnCDXlNeq16jXkNeV16og16LXnCDXl9eZ16TXldepINeW15Q/INec15TXodeo15QNCjxo
dHRwczovL3d3dy55YWQyLmNvLmlsL215LWFsZXJ0cz91dG1fc291cmNlPW15QWxlcnRzUmVhbGVz
dGF0ZSZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1teUFsZXJ0c1JlbW92YWw+DQoNCtec
16nXkNec15XXqiDXldeR15nXqNeV16jXmdedINeg15XXodek15nXnSDXoNeZ16rXnywg15zXmdem
15XXqCDXkNeZ16rXoNeVINen16nXqCDXm9eQ158NCjxodHRwczovL3d3dy55YWQyLmNvLmlsL2Nv
bnRhY3R1cz4NCiAgW2ltYWdlOiB5YWQyXQ0KPGh0dHBzOi8vd3d3LnlhZDIuY28uaWw/dXRtX3Nv
dXJjZT1teUFsZXJ0cyZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj15YWQyPg0KICBbaW1h
Z2U6IG1haWxdDQo8aHR0cHM6Ly93d3cueWFkMi5jby5pbC9jb250YWN0dXM/dXRtX3NvdXJjZT1t
eUFsZXJ0cyZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1jb250YWN0Pg0KICBbaW1hZ2U6
IGZhY2Vib29rXSA8aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3lhZDJwYWdlPiAgIFtpbWFnZTog
Y291dHVyZV0NCjxodHRwczovL3d3dy55b3V0dWJlLmNvbS91c2VyL01lWWFkMj4gICBbaW1hZ2U6
IGluc3RhZ3JhbV0NCjxodHRwczovL3d3dy5pbnN0YWdyYW0uY29tL3lhZDJwYWdlP2lnc2hpZD10
ejhoOTl6aWtzeXA+DQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0NCg0K16DXmdeq158g
15zXpNeg15XXqiDXkNec15nXoNeVINeR157Xodek16ggMDMtNTUyMjIyMiA8Kzk3Mi0zLTU1MjIy
MjI+LteR15nXnteZ150g15DXsy3XlNezINeR15nXnyDXlNep16LXldeqDQo4OjAwLTE4OjAwLA0K
15HXmdee15kg15XXsyDXldei16jXkdeZINeX15Ig15HXmdefINeU16nXoteV16ogODowMC0xMzow
MC4NCg==
--0000000000008956e605e29b3c5b
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><br><br><div class=3D"gmail_quote"><div dir=3D"ltr" class=
=3D"gmail_attr">---------- Forwarded message ---------<br>From: <strong cla=
ss=3D"gmail_sendername" dir=3D"auto">Yad2</strong> <span dir=3D"auto">&lt;<=
a href=3D"mailto:info@yad2.co.il">info@yad2.co.il</a>&gt;</span><br>Date: W=
ed, 29 Jun 2022 at 19:57<br>=E2=80=AASubject: =D7=9E=D7=95=D7=93=D7=A2=D7=
=95=D7=AA =D7=97=D7=93=D7=A9=D7=95=D7=AA =D7=A9=D7=A2=D7=9C=D7=95 =D7=91=D7=
=90=D7=AA=D7=A8 =D7=99=D7=932=E2=80=AC<br>To:  &lt;<a href=3D"mailto:test.s=
tern206@gmail.com">test.test@gmail.com</a>&gt;<br></div><br><br><u></u>

   =20
       =20
       =20
       =20
       =20
   =20
    <div style=3D"background-color:#f9f9f9;margin:0">
       =20
        <div marginwidth=3D"0" marginheight=3D"0" style=3D"color:#000000;fo=
nt-family:Arial,Helvetica Neue,Helvetica,sans-serif;font-size:1em;margin:0;=
padding:0">
            <table bgcolor=3D"#f9f9f9" style=3D"border-collapse:separate;bo=
rder-spacing:0;width:100%">
                <tbody><tr style=3D"width:100%">
                    <td align=3D"center" style=3D"text-align:center">
                        <center>
                           =20
   =20
                            <p class=3D"MsoNormal" style=3D"display:none;ma=
x-height:0px;overflow:hidden">
                                =D7=9E=D7=95=D7=93=D7=A2=D7=95=D7=AA =D7=97=
=D7=93=D7=A9=D7=95=D7=AA =D7=A9=D7=A2=D7=9C=D7=95 =D7=A2=D7=91=D7=95=D7=A8
                            </p>
                           =20
                           =20
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">=D7=97=D7=93=D7=A8=D7=99=D7=9D:</span>
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">3 - 5</span>
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">|</span>
                           =20
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">=D7=9E=D7=97=D7=99=D7=A8:</span>
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">1,000,000 - 4,000,000</span>
                                <span class=3D"MsoNormal" style=3D"display:=
none;max-height:0px;overflow:hidden">|</span>
                           =20

                            <div style=3D"display:none;max-height:0px;overf=
low:hidden">
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                                =C2=A0=E2=80=8C=C2=A0=E2=80=8C=C2=A0=E2=80=
=8C
                            </div>

                            <p class=3D"MsoNormal" align=3D"center" style=
=3D"display:block;margin:0 0 25px 0">
                                <a href=3D"https://y2-notification-service.=
s3-eu-west-1.amazonaws.com/mails/my-alerts/6_29_2022/2033671514752.8767-85c=
ecae87a7baaa664786128e60e3abe.html" style=3D"color:#999999;text-decoration:=
none" target=3D"_blank">
                                <span class=3D"MsoNormal" style=3D"color:#9=
99999;font-weight:500;text-decoration:none">
                                    =D7=90=D7=9D =D7=90=D7=99=D7=A0=D7=9A =
=D7=A8=D7=95=D7=90=D7=94 =D7=9E=D7=99=D7=99=D7=9C =D7=96=D7=94 =D7=9B=D7=A8=
=D7=90=D7=95=D7=99 =D7=9C=D7=97=D7=A5 =D7=9B=D7=90=D7=9F
                                </span>
                                </a>
                            </p>
                        </center>
                    </td>
                </tr>

                <tr style=3D"width:100%">
                    <td style=3D"text-align:center">
                        <center>
                            <table width=3D"360" dir=3D"rtl" align=3D"cente=
r" bgcolor=3D"#FFFFFF" border=3D"0" cellpadding=3D"0" cellspacing=3D"0" sty=
le=3D"direction:rtl;margin:0 5px">
                                <tbody><tr style=3D"width:100%">
                                    <th style=3D"text-align:center">
                                       =20

<table cellpadding=3D"0" border=3D"0" cellspacing=3D"0" style=3D"width:100%=
">
    <tbody><tr>
        <td>
           =20


    <a href=3D"https://www.yad2.co.il?utm_source=3DmyAlertsRealestate&amp;u=
tm_medium=3Demail&amp;utm_campaign=3DLogo" target=3D"_blank">
        <table border=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"mi=
n-height:100px;padding:5px 0 0;width:100%">
            <tbody><tr>
                <th width=3D"10"></th>
                    <th align=3D"left" style=3D"text-align:left;vertical-al=
ign:bottom">
                        <img src=3D"https://y2-notification-service.s3-eu-w=
est-1.amazonaws.com/images/my-alerts/realestate.png" alt=3D"Yad2 Category B=
anner" style=3D"width:360px">
                    </th>
            </tr>
        </tbody></table>
    </a>


        </td>
    </tr>

    <tr>
        <td>
           =20
           =20
            <table border=3D"0" cellpadding=3D"10" cellspacing=3D"0" style=
=3D"border-collapse:collapse;table-layout:fixed;width:100%">
               =20
                <tbody><tr>
                    <td>
                       =20
                       =20
                            <p align=3D"right" class=3D"MsoNormal" style=3D=
"color:#ff7100;font-size:1em;font-weight:500;line-height:1.375em;margin:0 1=
5px 5px 0">
                                <strong>
                                    =D7=94=D7=99=D7=99 =D7=90=D7=9C=D7=95=
=D7=9F,
                                </strong>
                            </p>
                            <p align=3D"right" class=3D"MsoNormal" style=3D=
"font-size:0.95em;font-weight:400;margin:0 15px 5px 0">
                                =D7=9E=D7=A6=D7=90=D7=A0=D7=95 106 =D7=9E=
=D7=95=D7=93=D7=A2=D7=95=D7=AA =D7=97=D7=93=D7=A9=D7=95=D7=AA =D7=A9=D7=9E=
=D7=AA=D7=90=D7=99=D7=9E=D7=95=D7=AA =D7=9C=D7=97=D7=99=D7=A4=D7=95=D7=A9 =
=D7=A9=D7=9C=D7=9A:
                            </p>
                       =20
                    </td>
                </tr>

               =20
                <tr>
                    <td>
                       =20
                        <table bgcolor=3D"#f9f9f9" cellspacing=3D"0" cellpa=
dding=3D"10" width=3D"309" style=3D"background-color:#f9f9f9;margin-right:1=
5px;width:309px!important">
                            <tbody><tr>
                                <td>
                                   =20
                                        <p align=3D"right" class=3D"MsoNorm=
al" style=3D"color:#000000;font-size:0.9em;margin:0 0 10px">
                                            <strong>=D7=93=D7=99=D7=A8=D7=
=95=D7=AA =D7=9C=D7=9E=D7=9B=D7=99=D7=A8=D7=94 =D7=91=D7=9E=D7=A8=D7=9B=D7=
=96</strong>
                                        </p>
                                   =20
                                   =20
                                    <a class=3D"MsoNormal" style=3D"color:#=
000000;font-size:1em;font-weight:400;text-decoration-color:transparent">
                                        <p align=3D"right" dir=3D"rtl" clas=
s=3D"MsoNormal" style=3D"color:#000000;font-size:1em;font-weight:400;margin=
:0;text-decoration-color:transparent">
                                           =20
                                                <span class=3D"MsoNormal" s=
tyle=3D"color:#000000;font-size:1em;font-weight:400;text-decoration-color:t=
ransparent">=D7=97=D7=93=D7=A8=D7=99=D7=9D:</span>
                                                <span style=3D"color:#00000=
0">3 - 5</span>
                                                <span style=3D"color:#99999=
9">|</span>
                                           =20
                                                <span class=3D"MsoNormal" s=
tyle=3D"color:#000000;font-size:1em;font-weight:400;text-decoration-color:t=
ransparent">=D7=9E=D7=97=D7=99=D7=A8:</span>
                                                <span style=3D"color:#00000=
0">1,000,000 - 4,000,000</span>
                                                <span style=3D"color:#99999=
9;display:none">|</span>
                                           =20
                                        </p>
                                    </a>
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>


               =20
                <tr>
                    <td>
                       =20
                        <div align=3D"center" style=3D"display:block;text-a=
lign:center">
                            <center>
                               =20
                                    <table dir=3D"rtl" border=3D"0" cellpad=
ding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tbody><tr>
                                            <td>
                                                <table cellpadding=3D"0" ce=
llspacing=3D"0" style=3D"border:1px solid #eeeeee;width:100%">
                                                    <tbody><tr>
                                                        <td align=3D"center=
" width=3D"310" style=3D"text-align:center">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/vjegyjk9?topArea=3D2&amp;rooms=3D3-5&amp;price=3D10=
00000-4000000&amp;category=3Drealestate&amp;subCategory=3Dforsale&amp;isFro=
mMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAlertsRealestate&a=
mp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202206/29/2_1/o/y2_1_08219_20220629081953.jpeg?=
w=3D309&amp;h=3D150&amp;l=3D1&amp;c=3D3" alt=3D"">
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"color:#000000;direction:rtl!important;disp=
lay:inline;font-size:1.125em;line-height:1em;margin:0 15px 5px;padding:0;te=
xt-align:right;text-decoration:none">
                                                                <strong sty=
le=3D"direction:rtl!important;text-decoration:none">=E2=80=8F2,250,000=C2=
=A0=E2=82=AA</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal" style=3D"display:none">=D7=92=D7=9D =D7=91=D7=98=
=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"font-size:1em;font-weight:500;line-height:=
1em;margin:0 15px 5px;padding:0;text-align:right">
                                                                =D7=A1=D7=
=A2=D7=93=D7=99=D7=94 =D7=92=D7=90=D7=95=D7=9F 6
                                                            </p>
                                                            <a class=3D"Mso=
Normal" style=3D"color:#000000;font-size:1em;font-weight:400;text-decoratio=
n-color:transparent">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal" style=3D"color:#999999;font-size:1e=
m;font-weight:300;line-height:1em;margin:0 15px 5px;padding:0;text-align:ri=
ght">
                                                                    =D7=92=
=D7=A8=D7=99=D7=9F =D7=95=D7=A2=D7=9D | =D7=93=D7=99=D7=A8=D7=94 | 4 =D7=97=
=D7=93=D7=A8=D7=99=D7=9D | 80 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"width:100%">
                                                                <tbody><tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;fo=
nt-weight:500;line-height:1em;margin:0 15px 5px;padding:0;text-align:right;=
text-decoration-color:transparent">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/vjegyjk9?topArea=3D2&amp;rooms=3D3-=
5&amp;price=3D1000000-4000000&amp;category=3Drealestate&amp;subCategory=3Df=
orsale&amp;isFromMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAl=
ertsRealestate&amp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" class=
=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-weight:500;text-al=
ign:right;text-decoration-color:transparent" target=3D"_blank">
                                                                           =
     <span class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-we=
ight:500;text-align:right;text-decoration-color:transparent">=D7=9C=D7=A4=
=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal" style=3D"color:#000000;font-size:1em;font-weight:400;te=
xt-decoration-color:transparent">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal" style=3D"font-size:0.75em;line-heigh=
t:1em;margin:0 15px 5px;padding:0;text-align:left">
                                                                           =
    =20
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table=
>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </tbody></table>
                               =20
                                    <table dir=3D"rtl" border=3D"0" cellpad=
ding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tbody><tr>
                                            <td>
                                                <table cellpadding=3D"0" ce=
llspacing=3D"0" style=3D"border:1px solid #eeeeee;width:100%">
                                                    <tbody><tr>
                                                        <td align=3D"center=
" width=3D"310" style=3D"text-align:center">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/fc4ggfmq?topArea=3D2&amp;rooms=3D3-5&amp;price=3D10=
00000-4000000&amp;category=3Drealestate&amp;subCategory=3Dforsale&amp;isFro=
mMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAlertsRealestate&a=
mp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202206/28/2_1/o/y2_2_05672_20220628221706.jpeg?=
w=3D309&amp;h=3D150&amp;l=3D1&amp;c=3D3" alt=3D"">
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"color:#000000;direction:rtl!important;disp=
lay:inline;font-size:1.125em;line-height:1em;margin:0 15px 5px;padding:0;te=
xt-align:right;text-decoration:none">
                                                                <strong sty=
le=3D"direction:rtl!important;text-decoration:none">=E2=80=8F2,350,000=C2=
=A0=E2=82=AA</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal" style=3D"display:none">=D7=92=D7=9D =D7=91=D7=98=
=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"font-size:1em;font-weight:500;line-height:=
1em;margin:0 15px 5px;padding:0;text-align:right">
                                                                =D7=A6=D7=
=99=D7=A8=D7=9C=D7=A1=D7=95=D7=9F 22
                                                            </p>
                                                            <a class=3D"Mso=
Normal" style=3D"color:#000000;font-size:1em;font-weight:400;text-decoratio=
n-color:transparent">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal" style=3D"color:#999999;font-size:1e=
m;font-weight:300;line-height:1em;margin:0 15px 5px;padding:0;text-align:ri=
ght">
                                                                    =D7=AA=
=D7=A7=D7=95=D7=9E=D7=94 / =D7=A7=D7=A8=D7=99=D7=AA =D7=97=D7=96=D7=A0=D7=
=99 | =D7=92=D7=92/=D7=A4=D7=A0=D7=98=D7=94=D7=90=D7=95=D7=96 | 5 =D7=97=D7=
=93=D7=A8=D7=99=D7=9D | 160 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"width:100%">
                                                                <tbody><tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;fo=
nt-weight:500;line-height:1em;margin:0 15px 5px;padding:0;text-align:right;=
text-decoration-color:transparent">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/fc4ggfmq?topArea=3D2&amp;rooms=3D3-=
5&amp;price=3D1000000-4000000&amp;category=3Drealestate&amp;subCategory=3Df=
orsale&amp;isFromMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAl=
ertsRealestate&amp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" class=
=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-weight:500;text-al=
ign:right;text-decoration-color:transparent" target=3D"_blank">
                                                                           =
     <span class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-we=
ight:500;text-align:right;text-decoration-color:transparent">=D7=9C=D7=A4=
=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal" style=3D"color:#000000;font-size:1em;font-weight:400;te=
xt-decoration-color:transparent">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal" style=3D"font-size:0.75em;line-heigh=
t:1em;margin:0 15px 5px;padding:0;text-align:left">
                                                                           =
    =20
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table=
>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </tbody></table>
                               =20
                                    <table dir=3D"rtl" border=3D"0" cellpad=
ding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tbody><tr>
                                            <td>
                                                <table cellpadding=3D"0" ce=
llspacing=3D"0" style=3D"border:1px solid #eeeeee;width:100%">
                                                    <tbody><tr>
                                                        <td align=3D"center=
" width=3D"310" style=3D"text-align:center">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/7dkwa288?topArea=3D2&amp;rooms=3D3-5&amp;price=3D10=
00000-4000000&amp;category=3Drealestate&amp;subCategory=3Dforsale&amp;isFro=
mMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAlertsRealestate&a=
mp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202206/28/2_5/o/y2_1_GR9RGaCVbm_20220628.jpeg?w=
=3D309&amp;h=3D150&amp;l=3D1&amp;c=3D3" alt=3D"">
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"color:#000000;direction:rtl!important;disp=
lay:inline;font-size:1.125em;line-height:1em;margin:0 15px 5px;padding:0;te=
xt-align:right;text-decoration:none">
                                                                <strong sty=
le=3D"direction:rtl!important;text-decoration:none">=E2=80=8F1,690,000=C2=
=A0=E2=82=AA</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal" style=3D"display:none">=D7=92=D7=9D =D7=91=D7=98=
=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"font-size:1em;font-weight:500;line-height:=
1em;margin:0 15px 5px;padding:0;text-align:right">
                                                                =D7=94=D7=
=97=D7=A9=D7=9E=D7=95=D7=A0=D7=90=D7=99=D7=9D=20
                                                            </p>
                                                            <a class=3D"Mso=
Normal" style=3D"color:#000000;font-size:1em;font-weight:400;text-decoratio=
n-color:transparent">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal" style=3D"color:#999999;font-size:1e=
m;font-weight:300;line-height:1em;margin:0 15px 5px;padding:0;text-align:ri=
ght">
                                                                    =D7=9C=
=D7=91 =D7=94=D7=A2=D7=99=D7=A8 | =D7=93=D7=99=D7=A8=D7=94 | 3 =D7=97=D7=93=
=D7=A8=D7=99=D7=9D | 57 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"width:100%">
                                                                <tbody><tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;fo=
nt-weight:500;line-height:1em;margin:0 15px 5px;padding:0;text-align:right;=
text-decoration-color:transparent">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/7dkwa288?topArea=3D2&amp;rooms=3D3-=
5&amp;price=3D1000000-4000000&amp;category=3Drealestate&amp;subCategory=3Df=
orsale&amp;isFromMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAl=
ertsRealestate&amp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" class=
=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-weight:500;text-al=
ign:right;text-decoration-color:transparent" target=3D"_blank">
                                                                           =
     <span class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-we=
ight:500;text-align:right;text-decoration-color:transparent">=D7=9C=D7=A4=
=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal" style=3D"color:#000000;font-size:1em;font-weight:400;te=
xt-decoration-color:transparent">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal" style=3D"font-size:0.75em;line-heigh=
t:1em;margin:0 15px 5px;padding:0;text-align:left">
                                                                           =
     =D7=96=D7=9E=D7=99=D7=A8 =D7=A0=D7=93=D7=9C&quot;=D7=9F
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table=
>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </tbody></table>
                               =20
                                    <table dir=3D"rtl" border=3D"0" cellpad=
ding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tbody><tr>
                                            <td>
                                                <table cellpadding=3D"0" ce=
llspacing=3D"0" style=3D"border:1px solid #eeeeee;width:100%">
                                                    <tbody><tr>
                                                        <td align=3D"center=
" width=3D"310" style=3D"text-align:center">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/zn2sqe4q?topArea=3D2&amp;rooms=3D3-5&amp;price=3D10=
00000-4000000&amp;category=3Drealestate&amp;subCategory=3Dforsale&amp;isFro=
mMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAlertsRealestate&a=
mp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202206/28/2_5/o/y2_1_9WS60PDyHg_20220628.jpg?w=
=3D309&amp;h=3D150&amp;l=3D1&amp;c=3D3" alt=3D"">
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"color:#000000;direction:rtl!important;disp=
lay:inline;font-size:1.125em;line-height:1em;margin:0 15px 5px;padding:0;te=
xt-align:right;text-decoration:none">
                                                                <strong sty=
le=3D"direction:rtl!important;text-decoration:none">=E2=80=8F2,300,000=C2=
=A0=E2=82=AA</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal" style=3D"display:none">=D7=92=D7=9D =D7=91=D7=98=
=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal" style=3D"font-size:1em;font-weight:500;line-height:=
1em;margin:0 15px 5px;padding:0;text-align:right">
                                                                =D7=99=D7=
=A9=D7=A8=D7=90=D7=9C =D7=9E=D7=A8=D7=99=D7=96&#39;=D7=99=D7=9F=20
                                                            </p>
                                                            <a class=3D"Mso=
Normal" style=3D"color:#000000;font-size:1em;font-weight:400;text-decoratio=
n-color:transparent">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal" style=3D"color:#999999;font-size:1e=
m;font-weight:300;line-height:1em;margin:0 15px 5px;padding:0;text-align:ri=
ght">
                                                                    =D7=A6=
=D7=94=D7=9C=D7=95=D7=9F, =D7=A9=D7=99=D7=9B=D7=95=D7=A0=D7=99 =D7=97=D7=A1=
=D7=9B=D7=95=D7=9F | =D7=93=D7=99=D7=A8=D7=94 | 3 =D7=97=D7=93=D7=A8=D7=99=
=D7=9D | 84 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" cellspacing=3D"0" cellpadding=3D"0" style=3D"width:100%">
                                                                <tbody><tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;fo=
nt-weight:500;line-height:1em;margin:0 15px 5px;padding:0;text-align:right;=
text-decoration-color:transparent">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/zn2sqe4q?topArea=3D2&amp;rooms=3D3-=
5&amp;price=3D1000000-4000000&amp;category=3Drealestate&amp;subCategory=3Df=
orsale&amp;isFromMyAlerts=3Dtrue&amp;myAlertsSort=3D1&amp;utm_source=3DmyAl=
ertsRealestate&amp;utm_medium=3Demail&amp;utm_campaign=3DmyAlertsAd" class=
=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-weight:500;text-al=
ign:right;text-decoration-color:transparent" target=3D"_blank">
                                                                           =
     <span class=3D"MsoNormal" style=3D"color:#ff7100;font-size:1em;font-we=
ight:500;text-align:right;text-decoration-color:transparent">=D7=9C=D7=A4=
=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal" style=3D"color:#000000;font-size:1em;font-weight:400;te=
xt-decoration-color:transparent">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal" style=3D"font-size:0.75em;line-heigh=
t:1em;margin:0 15px 5px;padding:0;text-align:left">
                                                                           =
     =D7=93=D7=A0=D7=99=D7=94 - URBANIX
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </tbody></table=
>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </tbody></table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </tbody></table>
                               =20
                            </center>
                        </div>
                    </td>
                </tr>


               =20
                <tr>
                    <td>
                       =20
                       =20
                            <div align=3D"center" style=3D"font-size:1em;ma=
rgin:0;text-align:center">
                                <center>
                                    <table border=3D"0" cellpadding=3D"2" c=
ellspacing=3D"3" bgcolor=3D"#FF7100" style=3D"max-width:120px">
                                        <tbody><tr>
                                            <td style=3D"text-align:center"=
>
                                                <a href=3D"https://www.yad2=
.co.il/realestate/forsale?topArea=3D2&amp;rooms=3D3-5&amp;price=3D1000000-4=
000000&amp;startDate=3D1656435424236-1656521824236&amp;myAlertsSort=3D1&amp=
;utm_source=3DmyAlertsRealestate&amp;utm_medium=3Demail&amp;utm_campaign=3D=
myAlertsFeed" class=3D"MsoNormal" style=3D"display:block;padding:6px;text-d=
ecoration-color:transparent" target=3D"_blank">
                                                    <span class=3D"MsoNorma=
l" style=3D"color:#ffffff;font-size:1em;text-align:center;text-decoration-c=
olor:transparent">=D7=9C=D7=9B=D7=9C =D7=94=D7=9E=D7=95=D7=93=D7=A2=D7=95=
=D7=AA</span>
                                                </a>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </center>
                            </div>
                       =20
                    </td>
                </tr>

               =20
                <tr>
                    <td>
                       =20

    <div align=3D"center" class=3D"MsoNormal">
        <center>
            <table bgcolor=3D"#363636" align=3D"center" class=3D"MsoNormal"=
 cellpadding=3D"5" cellspacing=3D"0" border=3D"0" style=3D"background-color=
:#363636;text-align:center;width:100%">
                <tbody><tr align=3D"center">
                    <td align=3D"center">
                        <p class=3D"MsoNormal" style=3D"color:#999999;font-=
size:0.75em;margin:0 0 15px;margin-top:10px;padding:0">=D7=9C=D7=90 =D7=A8=
=D7=95=D7=A6=D7=94 =D7=9C=D7=A7=D7=91=D7=9C =D7=94=D7=AA=D7=A8=D7=90=D7=95=
=D7=AA =D7=A2=D7=9C =D7=97=D7=99=D7=A4=D7=95=D7=A9 =D7=96=D7=94?=20
                            <a class=3D"MsoNormal" href=3D"https://www.yad2=
.co.il/my-alerts?utm_source=3DmyAlertsRealestate&amp;utm_medium=3Demail&amp=
;utm_campaign=3DmyAlertsRemoval" style=3D"color:#ffffff;text-decoration:und=
erline" target=3D"_blank">=D7=9C=D7=94=D7=A1=D7=A8=D7=94</a>
                        </p>
                        <p class=3D"MsoNormal" style=3D"color:#999999;font-=
size:0.75em;margin:0 0 15px;padding:0">=D7=9C=D7=A9=D7=90=D7=9C=D7=95=D7=AA=
 =D7=95=D7=91=D7=99=D7=A8=D7=95=D7=A8=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=
=D7=99=D7=9D =D7=A0=D7=99=D7=AA=D7=9F,=20
                            <a class=3D"MsoNormal" href=3D"https://www.yad2=
.co.il/contactus" style=3D"color:#ffffff;text-decoration:underline" target=
=3D"_blank">=D7=9C=D7=99=D7=A6=D7=95=D7=A8 =D7=90=D7=99=D7=AA=D7=A0=D7=95 =
=D7=A7=D7=A9=D7=A8 =D7=9B=D7=90=D7=9F</a>
                        </p>
                    </td>
                </tr>
                <tr class=3D"MsoNormal" align=3D"center">
                    <td align=3D"center" dir=3D"rtl">
                        <span>=C2=A0</span>
                        <a href=3D"https://www.yad2.co.il?utm_source=3DmyAl=
erts&amp;utm_medium=3Demail&amp;utm_campaign=3Dyad2" class=3D"MsoNormal" st=
yle=3D"color:#ffffff;font-size:1em;text-align:center;text-decoration-color:=
transparent" target=3D"_blank">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/yad2.png" width=3D"35" height=
=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal" alt=3D"yad2">
                        </a>
                        <span>=C2=A0</span>
                        <a href=3D"https://www.yad2.co.il/contactus?utm_sou=
rce=3DmyAlerts&amp;utm_medium=3Demail&amp;utm_campaign=3Dcontact" class=3D"=
MsoNormal" style=3D"color:#ffffff;font-size:1em;text-align:center;text-deco=
ration-color:transparent" target=3D"_blank">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/mail.png" width=3D"35" height=
=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal" alt=3D"mail">
                        </a>
                        <span>=C2=A0</span>
                        <a href=3D"https://www.facebook.com/yad2page" class=
=3D"MsoNormal" style=3D"color:#ffffff;font-size:1em;text-align:center;text-=
decoration-color:transparent" target=3D"_blank">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/facebook.png" width=3D"35" heig=
ht=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal" alt=3D"facebook">
                        </a>
                        <span>=C2=A0</span>
                        <a href=3D"https://www.youtube.com/user/MeYad2" cla=
ss=3D"MsoNormal" style=3D"color:#ffffff;font-size:1em;text-align:center;tex=
t-decoration-color:transparent" target=3D"_blank">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/youtube.png" width=3D"35" heigh=
t=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal" alt=3D"couture">
                        </a>
                        <span>=C2=A0</span>
                        <a href=3D"https://www.instagram.com/yad2page?igshi=
d=3Dtz8h99ziksyp" class=3D"MsoNormal" style=3D"color:#ffffff;font-size:1em;=
text-align:center;text-decoration-color:transparent" target=3D"_blank">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/instagram.png" width=3D"35" hei=
ght=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal" alt=3D"instagram">
                        </a>
                    </td>
                </tr>
                <tr>=20
                    <td>
                        <hr>
                        <p class=3D"MsoNormal" style=3D"color:#999999;font-=
size:0.75em;margin:0 0 15px;padding:0">
                            =D7=A0=D7=99=D7=AA=D7=9F =D7=9C=D7=A4=D7=A0=D7=
=95=D7=AA =D7=90=D7=9C=D7=99=D7=A0=D7=95 =D7=91=D7=9E=D7=A1=D7=A4=D7=A8 <a =
href=3D"tel:+972-3-5522222" style=3D"color:#ffffff;text-decoration:underlin=
e" target=3D"_blank">03-5522222</a>.=D7=91=D7=99=D7=9E=D7=99=D7=9D
                            =D7=90=D7=B3-=D7=94=D7=B3 =D7=91=D7=99=D7=9F =
=D7=94=D7=A9=D7=A2=D7=95=D7=AA 8:00-18:00,
                            <br>
                            =D7=91=D7=99=D7=9E=D7=99 =D7=95=D7=B3 =D7=95=D7=
=A2=D7=A8=D7=91=D7=99 =D7=97=D7=92 =D7=91=D7=99=D7=9F =D7=94=D7=A9=D7=A2=D7=
=95=D7=AA 8:00-13:00.
                        </p>
                    </td>=20
                </tr>
            </tbody></table>
        </center>
    </div>


                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>
                                    </th>
                                </tr>
                            </tbody></table>
                        </center>
                    </td>
                </tr>
            </tbody></table>
        </div>
    </div>

</div></div>

--0000000000008956e605e29b3c5b--
"""

test_mail2 = """Return-Path: <test.test+caf_=test=realestate-tracker.com@gmail.com>
Received: from mail-lf1-f48.google.com (mail-lf1-f48.google.com [209.85.167.48])
 by inbound-smtp.eu-west-1.amazonaws.com with SMTP id qnq7ft1md20ivmcli3c1g2as0vj5mqq4p9nvvg81
 for test@realestate-tracker.com;
 Sat, 02 Jul 2022 17:10:40 +0000 (UTC)
Received-SPF: pass (spfCheck: domain of _spf.google.com designates 209.85.167.48 as permitted sender) client-ip=209.85.167.48; envelope-from=test.test+caf_=test=realestate-tracker.com@gmail.com; helo=mail-lf1-f48.google.com;
Authentication-Results: amazonses.com;
 spf=pass (spfCheck: domain of _spf.google.com designates 209.85.167.48 as permitted sender) client-ip=209.85.167.48; envelope-from=test.test+caf_=test=realestate-tracker.com@gmail.com; helo=mail-lf1-f48.google.com;
 dkim=pass header.i=@yad2.co.il;
 dkim=pass header.i=@amazonses.com;
 dmarc=pass header.from=yad2.co.il;
X-SES-RECEIPT: AEFBQUFBQUFBQUFGN2hLbk16Zk5MYTlUWTcwWXlsb2QwMlVkR21nTFplcXhaUUNPQURjQTc0VTk0R0RUbXhyNlZyMFY0SUtJWVVCRWplL3NGWThxaGtiOHd1ajdVY0dFS0wxNG50bDBvSmRyTkNjOHVib1o3bmxUUjBTRmptUEtqVkpWaXRCNDNSNGdGTGZZeVFUaVJDdkxmSExTTFY2VVVzY1Y0bzVDK3N6Ymg3NThOZWRZNEZqN2tzbU5KNXdZRHNVQ1ZKbnFyMDM4TjA0OENGNFVNYmZYdjdFUlp0amgrbVZXSHR0SjNqRDFoQzZuMkNWNGxxNkpIMUZJL3JFUlBMK1R1MkdSUlMwOUJISTNCeVUzbms2RjdlYXRXOUlsSEhDa3F5VXpjbkE0TTI2OXV1dStiejMxSmU5dlVoUE03NmN3R2xjU0tMNkxsWk54VjFHQWVWcEMrZGZwUzdPTzhFdS9VRTVwTjhtVEk5ZnBnWE9oWlBBPT0=
X-SES-DKIM-SIGNATURE: a=rsa-sha256; q=dns/txt; b=lIFqZtbjbCFW1bTTld3Jwywq2Dwh1qdfLCxTp462lGQao8KmNyD5p3Iyar0qLr7WeyBusCHG8I7F8En62pApV2aWBMwQX+enRHwexsY50iCd6mQ3Q0xx3udTbcTSM0X81UzG3wLs54DnLbKzgtI/Z/Ek89D8I/07Uw5QAIQRaMc=; c=relaxed/simple; s=ihchhvubuqgjsxyuhssfvqohv7z3u4hn; d=amazonses.com; t=1656781840; v=1; bh=DtfmYCTlPLJwuKovSRrXKFsb/d5vZfPJUln+WTfliGo=; h=From:To:Cc:Bcc:Subject:Date:Message-ID:MIME-Version:Content-Type:X-SES-RECEIPT;
Received: by mail-lf1-f48.google.com with SMTP id z21so8757074lfb.12
        for <test@realestate-tracker.com>; Sat, 02 Jul 2022 10:10:39 -0700 (PDT)
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20210112;
        h=x-gm-message-state:delivered-to:dkim-signature:dkim-signature:from
         :to:subject:mime-version:content-transfer-encoding:message-id:date
         :feedback-id;
        bh=CUSnBhgXuNCm6dqzz6M8QK76siQxNg/2otxWxCE3IAM=;
        b=TFHknR6epFnGpTmMFpiKqTw5JLx2uHKQPeYk9M2rLO4JDEKzNx+q/iy9W5RMkKdLxT
         KDEEv5LgfEmOPiSAXbjE8ZjlwVp8CBtKyc7MQhAVi59O/OA35xsLLW6knpbCASvhqzqg
         u+PHP/NsSWM6DN8aPaqfN+9wYPczKIC+XwzCD8s5J2TmMIGP06R4awBtjC4lvZOTHiQ5
         WaAe8jVOJSSEfDvcDZrLJueCdydBXdy/Q0nSOZa/q8HXZDXC4+oNs9T4ROVWSjTwFqIJ
         iVaIK0Eim9swiQReyn84fMAxFjfOdULaKwC42Ej8roI5vxXKFEOVq8dzMOYi/fB5vcFl
         5A5g==
X-Gm-Message-State: AJIora/lEobxDb6GzIZ5xYyqXOE7FN455q8qXLW4RsqEvy6INGmoV0qj
	EsQdQLXkaGUucB1Wvmk/uxPYi5geZg5T2QBimcZ+BVlDIYmlOBuPMw==
X-Received: by 2002:a05:6512:3053:b0:481:2241:7825 with SMTP id b19-20020a056512305300b0048122417825mr12305401lfb.522.1656781839038;
        Sat, 02 Jul 2022 10:10:39 -0700 (PDT)
X-Forwarded-To: test@realestate-tracker.com
X-Forwarded-For: test.test@gmail.com test@realestate-tracker.com
Delivered-To: test.test@gmail.com
Received: by 2002:a05:6500:1707:b0:149:d94f:1f25 with SMTP id g7csp1454200lqd;
        Sat, 2 Jul 2022 10:10:37 -0700 (PDT)
X-Google-Smtp-Source: AGRyM1uN3kwT4IJnf9z/LnlAMtluocc16Oc/mPnpjkkHyv9DaqRSLpAdBBse5k7cMcERdkHBFbr9
X-Received: by 2002:a1c:27c6:0:b0:39c:34a5:9f88 with SMTP id n189-20020a1c27c6000000b0039c34a59f88mr23646752wmn.94.1656781837457;
        Sat, 02 Jul 2022 10:10:37 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1656781837; cv=none;
        d=google.com; s=arc-20160816;
        b=L0kZxVGV+KbPoAlHuMU1KcymfeLhQMgNnfkA+SY9UwRg8qxXk+pSusviQmNv4VSdiE
         chaCIC057jmdf/hwASZj0KP+4nCORoDU85J12SwjSBcXNi2XrPn2iTguGnCLjJgOyjtS
         oBUXu4EiSzY6zLw2C+EH+L4Naa98yiTebciGaZlJ0rIfM+4EzbyecuG2/jFeVTdue9BV
         hgnixei8NGyGp8gGVQ6hpBZ0N4MV1/y8YasYaT9lXL3jiQU1d7N1D1HPeA6YQHOqkDIa
         BLjna+IVS9xc/Vet93CqEwwm5NlQNreuqMbLoKnOkr0JrIbNUmbL6GzDzgoYMeFv+w4M
         Fcvw==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=feedback-id:date:message-id:content-transfer-encoding:mime-version
         :subject:to:from:dkim-signature:dkim-signature;
        bh=CUSnBhgXuNCm6dqzz6M8QK76siQxNg/2otxWxCE3IAM=;
        b=tN/nmLGnYqAESA05herE5k+MQf8/4XojX+Z869KKiKj//grO8KISdFodppe0JvgZP6
         fEiOwevLyo+eAOKiuyJflwjK6J6EyEBzbsqd/7YKImTEbXnUjgsqViwDwnr0FitXVRTa
         P6+P0GNVzoTrFjil+dGyko3XtvAbGyca1SaN6IcptuHFRVndZvOq7byrQwdyz6LtQrKg
         Ze+ZBHzIu/lg/k3VXjFL1pPgKtg1x8uqSrp/6moynGo2QETYz9Mmz3gC5/lCc3hRX5sT
         uZKP8TciEyJQfGvyM1htQm3gkAmSivgfzpT07zuAoUIgTpxPlr3pXuqgNDebr8tGMt3/
         BxyA==
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@yad2.co.il header.s=wcgxtkefluaabze7gltmx4pvnwhkyljz header.b=iLrMeqq2;
       dkim=pass header.i=@amazonses.com header.s=ihchhvubuqgjsxyuhssfvqohv7z3u4hn header.b=Rhd29+VV;
       spf=neutral (google.com: 54.240.3.1 is neither permitted nor denied by best guess record for domain of 01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il) smtp.mailfrom=01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=yad2.co.il
Return-Path: <01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il>
Received: from a3-1.smtp-out.eu-west-1.amazonses.com (a3-1.smtp-out.eu-west-1.amazonses.com. [54.240.3.1])
        by mx.google.com with ESMTPS id o8-20020a5d47c8000000b0020d0c15bbc5si16604647wrc.892.2022.07.02.10.10.37
        for <test.test@gmail.com>
        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);
        Sat, 02 Jul 2022 10:10:37 -0700 (PDT)
Received-SPF: neutral (google.com: 54.240.3.1 is neither permitted nor denied by best guess record for domain of 01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il) client-ip=54.240.3.1;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@yad2.co.il header.s=wcgxtkefluaabze7gltmx4pvnwhkyljz header.b=iLrMeqq2;
       dkim=pass header.i=@amazonses.com header.s=ihchhvubuqgjsxyuhssfvqohv7z3u4hn header.b=Rhd29+VV;
       spf=neutral (google.com: 54.240.3.1 is neither permitted nor denied by best guess record for domain of 01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il) smtp.mailfrom=01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@support.yad2.co.il;
       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=yad2.co.il
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=wcgxtkefluaabze7gltmx4pvnwhkyljz; d=yad2.co.il; t=1656781836;
	h=From:To:Subject:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID:Date;
	bh=DtfmYCTlPLJwuKovSRrXKFsb/d5vZfPJUln+WTfliGo=;
	b=iLrMeqq2WyIJ31Ph0DGgB0sMU29XeAKMptxf4K2bMeNXPjNCXR+vfWivDkcZZJAJ
	mG9hJs8jlvVNzdXicoWtoUyTXfne2QBUhvgIuQTuhrDXFMxKRMnUsZ0lH1uyYQr4aTj
	Xf07CnHLD69vCMIr8xHpYpL26XNcvJTIbJZEka80=
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
	s=ihchhvubuqgjsxyuhssfvqohv7z3u4hn; d=amazonses.com; t=1656781836;
	h=From:To:Subject:MIME-Version:Content-Type:Content-Transfer-Encoding:Message-ID:Date:Feedback-ID;
	bh=DtfmYCTlPLJwuKovSRrXKFsb/d5vZfPJUln+WTfliGo=;
	b=Rhd29+VVlUKHlBpZU9d0XfZES6YT2Z/hyRjzU4eWcwBt8KqBJg8pJeCckHKyJxPU
	iM2RgW+sSwOcjdY3brdhXmZjFIRAA6i//KbYf1+3za6kBVCgL1Lu7Di5Ckf3ZiKlkqR
	IThmlKuA7beuqxGTULDU5/bOwaA1E9gKIy54q+yM=
From: Yad2 <info@yad2.co.il>
To: test.test@gmail.com
Subject: =?UTF-8?B?157XldeT16LXldeqINeX15PXqdeV16og?=
 =?UTF-8?B?16nXotec15Ug15HXkNeq16gg15nXkzI=?=
MIME-Version: 1.0
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable
Message-ID: <01020181bfe4921c-19f0b1ab-465b-43c1-9deb-fcd500dabf2c-000000@eu-west-1.amazonses.com>
Date: Sat, 2 Jul 2022 17:10:36 +0000
Feedback-ID: 1.eu-west-1.YeaVoV7RmSVVK1vdIvUKdQ0dASQrtg+Nog6D+GFV3JI=:AmazonSES
X-SES-Outgoing: 2022.07.02-54.240.3.1

<!doctype html>
<html =E2=9A=A14email>
    <head>
        <title>y2-mail-restore</title>
        <meta charset=3D"UTF-8">
        <meta name=3D"viewport" content=3D"width=3Ddevice-width, initial-sc=
ale=3D1">
        <style>
            body {
                background-color: #f9f9f9;
                margin: 0;
            }
        </style>
    </head>
    <body style=3D"background-color: #f9f9f9; margin: 0;">
        <style>
            .y2_mail_body {
                font-size: 1em;
                color: #000000;
                margin: 0;
                padding: 0;
                font-family: Arial,Helvetica Neue,Helvetica,sans-serif;
            }
            .y2_mail_table {
                width: 100%;
                border-spacing: 0;
                border-collapse: separate;
            }
            .y2_mail_row {
                width: 100%;
            }
            .y2_mail_col {
                text-align: center;
            }
            .restore_link_p {
                display: none;
            }
            .restore_link {
                color: #999999;
                text-decoration: none;
            }
            .link_font {
                color:#999999;
                font-weight: 500;
            }
            .no_under {
                text-decoration: none !important;
                text-decoration: none;
            }
            .content_outer_wrapper {
                margin: 0 5px;
                direction: rtl;
            }
        </style>
        <div marginwidth=3D"0" marginheight=3D"0" class=3D"y2_mail_body" st=
yle=3D"color: #000000; font-family: Arial,Helvetica Neue,Helvetica,sans-ser=
if; font-size: 1em; margin: 0; padding: 0;">
            <table bgcolor=3D"#f9f9f9" class=3D"y2_mail_table" style=3D"bor=
der-collapse: separate; border-spacing: 0; width: 100%;">
                <tr class=3D"y2_mail_row" style=3D"width: 100%;">
                    <td align=3D"center" class=3D"y2_mail_col" style=3D"tex=
t-align: center;">
                        <center>
                            <style>
                                .preview_text {
                                    display: none;
                                    max-height: 0px;
                                    overflow: hidden;
                                }
                                .preview_text_whitespace {
                                    display: none;
                                    max-height: 0px;
                                    overflow: hidden;
                                }
                            </style>
   =20
                            <p class=3D"MsoNormal preview_text" style=3D"di=
splay: none; max-height: 0px; overflow: hidden;">
                                =D7=9E=D7=95=D7=93=D7=A2=D7=95=D7=AA =D7=97=
=D7=93=D7=A9=D7=95=D7=AA =D7=A9=D7=A2=D7=9C=D7=95 =D7=A2=D7=91=D7=95=D7=A8
                            </p>
                           =20
                           =20
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">=D7=97=D7=93=D7=A8=
=D7=99=D7=9D:</span>
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">3 - 5</span>
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">|</span>
                           =20
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">=D7=9E=D7=97=D7=99=
=D7=A8:</span>
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">1,000,000 - 4,000,0=
00</span>
                                <span class=3D"MsoNormal preview_text" styl=
e=3D"display: none; max-height: 0px; overflow: hidden;">|</span>
                           =20

                            <div class=3D"preview_text_whitespace" style=3D=
"display: none; max-height: 0px; overflow: hidden;">
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                                &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
                            </div>

                            <p class=3D"MsoNormal restore_link_p" align=3D"=
center" style=3D"display: block; margin: 0 0 25px 0;">
                                <a class=3D"restore_link link-no-decoration=
" target=3D"_blank" href=3D"https://y2-notification-service.s3-eu-west-1.am=
azonaws.com/mails/my-alerts/7_2_2022/3847398854756.245-9ea2cce91cafd0d2f7a8=
929a94538cb5.html" style=3D"color: #999999; text-decoration: none;">
                                <span class=3D"MsoNormal link_font no_under=
" style=3D"color: #999999; font-weight: 500; text-decoration: none;">
                                    =D7=90=D7=9D =D7=90=D7=99=D7=A0=D7=9A =
=D7=A8=D7=95=D7=90=D7=94 =D7=9E=D7=99=D7=99=D7=9C =D7=96=D7=94 =D7=9B=D7=A8=
=D7=90=D7=95=D7=99 =D7=9C=D7=97=D7=A5 =D7=9B=D7=90=D7=9F
                                </span>
                                </a>
                            </p>
                        </center>
                    </td>
                </tr>

                <tr class=3D"y2_mail_row" style=3D"width: 100%;">
                    <td class=3D"y2_mail_col" style=3D"text-align: center;"=
>
                        <center>
                            <table class=3D"content_outer_wrapper" width=3D=
"360" dir=3D"rtl" align=3D"center" bgcolor=3D"#FFFFFF" border=3D"0" cellpad=
ding=3D"0" cellspacing=3D"0" style=3D"direction: rtl; margin: 0 5px;">
                                <tr class=3D"y2_mail_row" style=3D"width: 1=
00%;">
                                    <th class=3D"y2_mail_col" style=3D"text=
-align: center;">
                                        <style>
    .alert_content {
        width: 100%;
    }
</style>

<table class=3D"alert_content" cellpadding=3D"0" border=3D"0" cellspacing=
=3D"0" style=3D"width: 100%;">
    <tr>
        <td>
            <!-- My Alerts Category Header -->
<style>
    .alert_category_header {
        padding: 5px 0 0;
        width: 100%;
        min-height: 100px;
    }
    .category_header_text {
        color: #FFFFFF;
        font-weight: 800;
        font-size: 1.125em;
        margin: 0;
    }
    .category_image_container {
        text-align: left;
        vertical-align: bottom;
    }

    .vehicles,.realestate {
        width: 360px;

    }

</style>

    <a href=3D"https://www.yad2.co.il?utm_source=3DmyAlertsRealestate&utm_m=
edium=3Demail&utm_campaign=3DLogo">
        <table class=3D"alert_category_header" border=3D"0" cellspacing=3D"=
0" cellpadding=3D"0" style=3D"min-height: 100px; padding: 5px 0 0; width: 1=
00%;">
            <tr>
                <th width=3D"10"></th>
                    <th align=3D"left" class=3D"category_image_container" s=
tyle=3D"text-align: left; vertical-align: bottom;">
                        <img src=3D"https://y2-notification-service.s3-eu-w=
est-1.amazonaws.com/images/my-alerts/realestate.png" alt=3D"Yad2 Category B=
anner" class=3D"realestate" style=3D"width: 360px;">
                    </th>
            </tr>
        </table>
    </a>


        </td>
    </tr>

    <tr>
        <td>
            <!-- My Alerts Content -->
            <style>
                .inner_alert_content {
                    width: 100%;
                    border-collapse: collapse;
                    table-layout: fixed;
                }
            </style>
            <table class=3D"inner_alert_content" border=3D"0" cellpadding=
=3D"10" cellspacing=3D"0" style=3D"border-collapse: collapse; table-layout:=
 fixed; width: 100%;">
                <!-- Greeting Section -->
                <tr>
                    <td>
                        <style>
                            .greeting_line {
                                color: #ff7100;
                                font-size: 1em;
                                font-weight: 500;
                                line-height: 1.375em;
                            }
                            .greeting_info {
                                font-weight: 400;
                                font-size: 0.95em;
                            }
                            .greeting_line, .greeting_info {
                                margin: 0 15px 5px 0;
                            }
                        </style>
                       =20
                            <p align=3D"right" class=3D"MsoNormal greeting_=
line" style=3D"color: #ff7100; font-size: 1em; font-weight: 500; line-heigh=
t: 1.375em; margin: 0 15px 5px 0;">
                                <strong>
                                    =D7=94=D7=99=D7=99 =D7=90=D7=9C=D7=95=
=D7=9F,
                                </strong>
                            </p>
                            <p align=3D"right" class=3D"MsoNormal greeting_=
info" style=3D"font-size: 0.95em; font-weight: 400; margin: 0 15px 5px 0;">
                                =D7=9E=D7=A6=D7=90=D7=A0=D7=95 20 =D7=9E=D7=
=95=D7=93=D7=A2=D7=95=D7=AA =D7=97=D7=93=D7=A9=D7=95=D7=AA =D7=A9=D7=9E=D7=
=AA=D7=90=D7=99=D7=9E=D7=95=D7=AA =D7=9C=D7=97=D7=99=D7=A4=D7=95=D7=A9 =D7=
=A9=D7=9C=D7=9A:
                            </p>
                       =20
                    </td>
                </tr>

                <!-- Filters Section -->
                <tr>
                    <td>
                        <style>
                            .alert_filters {
                                background-color: #f9f9f9;
                                margin-right: 15px;
                            }
                            .alert_filters_title {
                                color: #000000;
                                margin: 0 0 10px;
                                font-size: 0.9em;
                            }
                            .alert_filters_content {
                                font-size: 0.87em;
                                font-weight: 400;
                                margin: 0;
                            }
                            .alert_filter_label {
                                color: #999999;
                            }
                            .alert_filter_placeholder {
                                color: #000000;
                            }
                            .alert_filter_seperator {
                                color: #999999;
                            }
                            .alert_filters_content .alert_filter_seperator:=
last-child {
                                display: none;
                            }
                            .no_under_number {
                                text-decoration-color: transparent;
                                pointer-events: none;
                                color:#000000;
                            }
                        </style>
                        <table class=3D"alert_filters" bgcolor=3D"#f9f9f9" =
cellspacing=3D"0" cellpadding=3D"10" width=3D"309" style=3D"background-colo=
r: #f9f9f9; margin-right: 15px; width: 309px !important;">
                            <tr>
                                <td>
                                   =20
                                        <p align=3D"right" class=3D"MsoNorm=
al alert_filters_title" style=3D"color: #000000; font-size: 0.9em; margin: =
0 0 10px;">
                                            <strong>=D7=93=D7=99=D7=A8=D7=
=95=D7=AA =D7=9C=D7=9E=D7=9B=D7=99=D7=A8=D7=94 =D7=91=D7=9E=D7=A8=D7=9B=D7=
=96</strong>
                                        </p>
                                   =20
                                   =20
                                    <a class=3D"MsoNormal no_under_number" =
style=3D"color: #000000; font-size: 1em; font-weight: 400; pointer-events: =
none; text-decoration-color: transparent;">
                                        <p align=3D"right" dir=3D"rtl" clas=
s=3D"MsoNormal alert_filters_content no_under_number" style=3D"color: #0000=
00; font-size: 1em; font-weight: 400; margin: 0; pointer-events: none; text=
-decoration-color: transparent;">
                                           =20
                                                <span class=3D"MsoNormal al=
ert_filter_label no_under_number" style=3D"color: #000000; font-size: 1em; =
font-weight: 400; pointer-events: none; text-decoration-color: transparent;=
">=D7=97=D7=93=D7=A8=D7=99=D7=9D:</span>
                                                <span class=3D"alert_filter=
_placeholder" style=3D"color: #000000;">3 - 5</span>
                                                <span class=3D"alert_filter=
_seperator" style=3D"color: #999999;">|</span>
                                           =20
                                                <span class=3D"MsoNormal al=
ert_filter_label no_under_number" style=3D"color: #000000; font-size: 1em; =
font-weight: 400; pointer-events: none; text-decoration-color: transparent;=
">=D7=9E=D7=97=D7=99=D7=A8:</span>
                                                <span class=3D"alert_filter=
_placeholder" style=3D"color: #000000;">1,000,000 - 4,000,000</span>
                                                <span class=3D"alert_filter=
_seperator" style=3D"color: #999999; display: none;">|</span>
                                           =20
                                        </p>
                                    </a>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>


                <!-- Feed Section -->
                <tr>
                    <td>
                        <style>
                            .alert_item_content {
                                width: 100%;
                                border: 1px solid #eeeeee;
                            }
                            .alert_item_content p {
                                margin: 0;
                            }
                            .price {
                                display: inline;
                                text-align: right;
                                font-size: 1.125em;
                                color: #000000;
                            }
                            .content_col p {
                                margin: 0 15px 5px;
                                line-height: 1em;
                                padding: 0;
                            }
                            .title {
                                text-align: right;
                                font-size: 1em;
                                font-weight: 500;
                            }
                            .item_filters {
                                text-align: right;
                                font-size: 1em;
                                font-weight: 300;
                                color: #999999;
                            }
                            .item_link {
                                text-align: right;
                                text-decoration-color: transparent;
                                font-size: 1em;
                                font-weight: 500;
                                color: #ff7100;
                            }
                            .feed_wrapper {
                                text-align: center;
                                display: block;
                            }
                            .image_column {
                                text-align: center;
                            }
                            .agency_name {
                                font-size: 0.75em;
                                text-align: left;
                            }
                            .bottom_content_section {
                                width: 100%;
                            }
                            .price, .price_text {
                                text-decoration:none;
                                pointer-events: none;
                                cursor: default;
                                direction: rtl !important;
                            }
                            .no_under_number {
                                text-decoration-color: transparent;
                                pointer-events: none;
                                font-size: 1em;
                                font-weight: 400;
                            }
                            .trade_in.true{
                                display:inline;
                                margin: 0 10px;
                                float: left;
                                color:#fff;
                                background-color:#40cf78;
                                font-size:.85rem;
                                line-height:1.25rem;
                                font-weight:500;
                                border-radius:4px;
                                padding:1px 3px;
                                height:-webkit-fit-content;
                                height:-moz-fit-content;
                                height:fit-content;
                                line-height:normal;
                                width:-webkit-fit-content;
                                width:-moz-fit-content;
                                width:fit-content
                            }
                            .trade_in {
                                display: none;
                            }

                        </style>
                        <div align=3D"center" class=3D"feed_wrapper" style=
=3D"display: block; text-align: center;">
                            <center>
                               =20
                                    <table dir=3D"rtl" class=3D"alert_item"=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tr>
                                            <td>
                                                <table class=3D"alert_item_=
content" cellpadding=3D"0" cellspacing=3D"0" style=3D"border: 1px solid #ee=
eeee; width: 100%;">
                                                    <tr>
                                                        <td align=3D"center=
" class=3D"image_column" width=3D"310" style=3D"text-align: center;">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/w6srvonb?topArea=3D2&rooms=3D3-5&price=3D1000000-40=
00000&category=3Drealestate&subCategory=3Dforsale&isFromMyAlerts=3Dtrue&myA=
lertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3Demail&utm_campai=
gn=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202207/02/2_1/o/y2_1_06847_20220702124911.jpeg?=
w=3D309&h=3D150&l=3D1&c=3D3" alt>
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td class=3D"conten=
t_col">
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal price" style=3D"color: #000000; cursor: default; dir=
ection: rtl !important; display: inline; font-size: 1.125em; line-height: 1=
em; margin: 0 15px 5px; padding: 0; pointer-events: none; text-align: right=
; text-decoration: none;">
                                                                <strong cla=
ss=3D"price_text" style=3D"cursor: default; direction: rtl !important; poin=
ter-events: none; text-decoration: none;">=E2=80=8F2,300,000=C2=A0=E2=82=AA=
</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal trade_in {{isTradeInButtonPackage}}" style=3D"disp=
lay: none;">=D7=92=D7=9D =D7=91=D7=98=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=
=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal title" style=3D"font-size: 1em; font-weight: 500; li=
ne-height: 1em; margin: 0 15px 5px; padding: 0; text-align: right;">
                                                                =D7=90=D7=
=99=D7=9C=D7=AA 22
                                                            </p>
                                                            <a class=3D"Mso=
Normal no_under_number" style=3D"color: #000000; font-size: 1em; font-weigh=
t: 400; pointer-events: none; text-decoration-color: transparent;">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal item_filters" style=3D"color: #99999=
9; font-size: 1em; font-weight: 300; line-height: 1em; margin: 0 15px 5px; =
padding: 0; text-align: right;">
                                                                    =D7=A0=
=D7=90=D7=95=D7=AA =D7=A8=D7=97=D7=9C | =D7=93=D7=99=D7=A8=D7=94 | 4.5 =D7=
=97=D7=93=D7=A8=D7=99=D7=9D | 120 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" class=3D"bottom_content_section" cellspacing=3D"0" cellpadding=3D"0"=
 style=3D"width: 100%;">
                                                                <tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal item_link" style=3D"color: #ff7100; font=
-size: 1em; font-weight: 500; line-height: 1em; margin: 0 15px 5px; padding=
: 0; text-align: right; text-decoration-color: transparent;">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/w6srvonb?topArea=3D2&rooms=3D3-5&pr=
ice=3D1000000-4000000&category=3Drealestate&subCategory=3Dforsale&isFromMyA=
lerts=3Dtrue&myAlertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3D=
email&utm_campaign=3DmyAlertsAd" class=3D"MsoNormal item_link" target=3D"_b=
lank" style=3D"color: #ff7100; font-size: 1em; font-weight: 500; text-align=
: right; text-decoration-color: transparent;">
                                                                           =
     <span class=3D"MsoNormal item_link" style=3D"color: #ff7100; font-size=
: 1em; font-weight: 500; text-align: right; text-decoration-color: transpar=
ent;">=D7=9C=D7=A4=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=
=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal no_under_number" style=3D"color: #000000; font-size: 1em=
; font-weight: 400; pointer-events: none; text-decoration-color: transparen=
t;">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal agency_name" style=3D"font-size: 0.75=
em; line-height: 1em; margin: 0 15px 5px; padding: 0; text-align: left;">
                                                                           =
    =20
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </table>
                               =20
                                    <table dir=3D"rtl" class=3D"alert_item"=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tr>
                                            <td>
                                                <table class=3D"alert_item_=
content" cellpadding=3D"0" cellspacing=3D"0" style=3D"border: 1px solid #ee=
eeee; width: 100%;">
                                                    <tr>
                                                        <td align=3D"center=
" class=3D"image_column" width=3D"310" style=3D"text-align: center;">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/126jkwvi?topArea=3D2&rooms=3D3-5&price=3D1000000-40=
00000&category=3Drealestate&subCategory=3Dforsale&isFromMyAlerts=3Dtrue&myA=
lertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3Demail&utm_campai=
gn=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202207/01/2_1/o/y2_1_09566_20220701174008.jpeg?=
w=3D309&h=3D150&l=3D1&c=3D3" alt>
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td class=3D"conten=
t_col">
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal price" style=3D"color: #000000; cursor: default; dir=
ection: rtl !important; display: inline; font-size: 1.125em; line-height: 1=
em; margin: 0 15px 5px; padding: 0; pointer-events: none; text-align: right=
; text-decoration: none;">
                                                                <strong cla=
ss=3D"price_text" style=3D"cursor: default; direction: rtl !important; poin=
ter-events: none; text-decoration: none;">=E2=80=8F1,299,000=C2=A0=E2=82=AA=
</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal trade_in {{isTradeInButtonPackage}}" style=3D"disp=
lay: none;">=D7=92=D7=9D =D7=91=D7=98=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=
=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal title" style=3D"font-size: 1em; font-weight: 500; li=
ne-height: 1em; margin: 0 15px 5px; padding: 0; text-align: right;">
                                                                =D7=A6=D7=
=94"=D7=9C 13
                                                            </p>
                                                            <a class=3D"Mso=
Normal no_under_number" style=3D"color: #000000; font-size: 1em; font-weigh=
t: 400; pointer-events: none; text-decoration-color: transparent;">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal item_filters" style=3D"color: #99999=
9; font-size: 1em; font-weight: 300; line-height: 1em; margin: 0 15px 5px; =
padding: 0; text-align: right;">
                                                                    =D7=90=
=D7=A9=D7=9B=D7=95=D7=9C | =D7=93=D7=99=D7=A8=D7=94 | 3.5 =D7=97=D7=93=D7=
=A8=D7=99=D7=9D | 70 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" class=3D"bottom_content_section" cellspacing=3D"0" cellpadding=3D"0"=
 style=3D"width: 100%;">
                                                                <tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal item_link" style=3D"color: #ff7100; font=
-size: 1em; font-weight: 500; line-height: 1em; margin: 0 15px 5px; padding=
: 0; text-align: right; text-decoration-color: transparent;">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/126jkwvi?topArea=3D2&rooms=3D3-5&pr=
ice=3D1000000-4000000&category=3Drealestate&subCategory=3Dforsale&isFromMyA=
lerts=3Dtrue&myAlertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3D=
email&utm_campaign=3DmyAlertsAd" class=3D"MsoNormal item_link" target=3D"_b=
lank" style=3D"color: #ff7100; font-size: 1em; font-weight: 500; text-align=
: right; text-decoration-color: transparent;">
                                                                           =
     <span class=3D"MsoNormal item_link" style=3D"color: #ff7100; font-size=
: 1em; font-weight: 500; text-align: right; text-decoration-color: transpar=
ent;">=D7=9C=D7=A4=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=
=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal no_under_number" style=3D"color: #000000; font-size: 1em=
; font-weight: 400; pointer-events: none; text-decoration-color: transparen=
t;">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal agency_name" style=3D"font-size: 0.75=
em; line-height: 1em; margin: 0 15px 5px; padding: 0; text-align: left;">
                                                                           =
    =20
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </table>
                               =20
                                    <table dir=3D"rtl" class=3D"alert_item"=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tr>
                                            <td>
                                                <table class=3D"alert_item_=
content" cellpadding=3D"0" cellspacing=3D"0" style=3D"border: 1px solid #ee=
eeee; width: 100%;">
                                                    <tr>
                                                        <td align=3D"center=
" class=3D"image_column" width=3D"310" style=3D"text-align: center;">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/eeo3xrv2?topArea=3D2&rooms=3D3-5&price=3D1000000-40=
00000&category=3Drealestate&subCategory=3Dforsale&isFromMyAlerts=3Dtrue&myA=
lertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3Demail&utm_campai=
gn=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202207/02/2_5/o/y2_1_Chrmt2bfsm_20220702.jpg?w=
=3D309&h=3D150&l=3D1&c=3D3" alt>
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td class=3D"conten=
t_col">
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal price" style=3D"color: #000000; cursor: default; dir=
ection: rtl !important; display: inline; font-size: 1.125em; line-height: 1=
em; margin: 0 15px 5px; padding: 0; pointer-events: none; text-align: right=
; text-decoration: none;">
                                                                <strong cla=
ss=3D"price_text" style=3D"cursor: default; direction: rtl !important; poin=
ter-events: none; text-decoration: none;">=E2=80=8F2,180,000=C2=A0=E2=82=AA=
</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal trade_in {{isTradeInButtonPackage}}" style=3D"disp=
lay: none;">=D7=92=D7=9D =D7=91=D7=98=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=
=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal title" style=3D"font-size: 1em; font-weight: 500; li=
ne-height: 1em; margin: 0 15px 5px; padding: 0; text-align: right;">
                                                                =D7=A2=D7=
=A5 =D7=94=D7=90=D7=A4=D7=A8=D7=A1=D7=A7 6
                                                            </p>
                                                            <a class=3D"Mso=
Normal no_under_number" style=3D"color: #000000; font-size: 1em; font-weigh=
t: 400; pointer-events: none; text-decoration-color: transparent;">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal item_filters" style=3D"color: #99999=
9; font-size: 1em; font-weight: 300; line-height: 1em; margin: 0 15px 5px; =
padding: 0; text-align: right;">
                                                                    =D7=A0=
=D7=95=D7=95=D7=94 =D7=A2=D7=95=D7=91=D7=93 | =D7=93=D7=99=D7=A8=D7=94 | 4 =
=D7=97=D7=93=D7=A8=D7=99=D7=9D | 100 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" class=3D"bottom_content_section" cellspacing=3D"0" cellpadding=3D"0"=
 style=3D"width: 100%;">
                                                                <tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal item_link" style=3D"color: #ff7100; font=
-size: 1em; font-weight: 500; line-height: 1em; margin: 0 15px 5px; padding=
: 0; text-align: right; text-decoration-color: transparent;">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/eeo3xrv2?topArea=3D2&rooms=3D3-5&pr=
ice=3D1000000-4000000&category=3Drealestate&subCategory=3Dforsale&isFromMyA=
lerts=3Dtrue&myAlertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3D=
email&utm_campaign=3DmyAlertsAd" class=3D"MsoNormal item_link" target=3D"_b=
lank" style=3D"color: #ff7100; font-size: 1em; font-weight: 500; text-align=
: right; text-decoration-color: transparent;">
                                                                           =
     <span class=3D"MsoNormal item_link" style=3D"color: #ff7100; font-size=
: 1em; font-weight: 500; text-align: right; text-decoration-color: transpar=
ent;">=D7=9C=D7=A4=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=
=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal no_under_number" style=3D"color: #000000; font-size: 1em=
; font-weight: 400; pointer-events: none; text-decoration-color: transparen=
t;">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal agency_name" style=3D"font-size: 0.75=
em; line-height: 1em; margin: 0 15px 5px; padding: 0; text-align: left;">
                                                                           =
     =D7=94=D7=A0=D7=93=D7=9C"=D7=9F =D7=A9=D7=9C =D7=93=D7=9F
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </table>
                               =20
                                    <table dir=3D"rtl" class=3D"alert_item"=
 border=3D"0" cellpadding=3D"0" cellspacing=3D"0" width=3D"309">
                                        <tr>
                                            <td>
                                                <table class=3D"alert_item_=
content" cellpadding=3D"0" cellspacing=3D"0" style=3D"border: 1px solid #ee=
eeee; width: 100%;">
                                                    <tr>
                                                        <td align=3D"center=
" class=3D"image_column" width=3D"310" style=3D"text-align: center;">
                                                            <a href=3D"http=
s://www.yad2.co.il/item/oqv49v63?topArea=3D2&rooms=3D3-5&price=3D1000000-40=
00000&category=3Drealestate&subCategory=3Dforsale&isFromMyAlerts=3Dtrue&myA=
lertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3Demail&utm_campai=
gn=3DmyAlertsAd" target=3D"_blank">
                                                                <img src=3D=
"https://img.yad2.co.il/Pic/202207/02/2_5/o/y2_1_m2akjKO4_V_20220702.jpeg?w=
=3D309&h=3D150&l=3D1&c=3D3" alt>
                                                            </a>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>

                                                    <tr>
                                                        <td class=3D"conten=
t_col">
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal price" style=3D"color: #000000; cursor: default; dir=
ection: rtl !important; display: inline; font-size: 1.125em; line-height: 1=
em; margin: 0 15px 5px; padding: 0; pointer-events: none; text-align: right=
; text-decoration: none;">
                                                                <strong cla=
ss=3D"price_text" style=3D"cursor: default; direction: rtl !important; poin=
ter-events: none; text-decoration: none;">=E2=80=8F3,990,000=C2=A0=E2=82=AA=
</strong>
                                                            </p>
                                                            <span align=3D"=
left" class=3D"MsoNormal trade_in {{isTradeInButtonPackage}}" style=3D"disp=
lay: none;">=D7=92=D7=9D =D7=91=D7=98=D7=A8=D7=99=D7=99=D7=93 =D7=90=D7=99=
=D7=9F</span>
                                                            <p align=3D"rig=
ht" class=3D"MsoNormal title" style=3D"font-size: 1em; font-weight: 500; li=
ne-height: 1em; margin: 0 15px 5px; padding: 0; text-align: right;">
                                                                =20
                                                            </p>
                                                            <a class=3D"Mso=
Normal no_under_number" style=3D"color: #000000; font-size: 1em; font-weigh=
t: 400; pointer-events: none; text-decoration-color: transparent;">
                                                                <p align=3D=
"right" dir=3D"rtl" class=3D"MsoNormal item_filters" style=3D"color: #99999=
9; font-size: 1em; font-weight: 300; line-height: 1em; margin: 0 15px 5px; =
padding: 0; text-align: right;">
                                                                    =D7=A0=
=D7=97=D7=9C=D7=AA =D7=92=D7=A0=D7=99=D7=9D | =D7=93=D7=99=D7=A8=D7=AA =D7=
=92=D7=9F | 4 =D7=97=D7=93=D7=A8=D7=99=D7=9D | 210 =D7=9E=D7=B4=D7=A8
                                                                </p>
                                                            </a>
                                                            <table border=
=3D"0" class=3D"bottom_content_section" cellspacing=3D"0" cellpadding=3D"0"=
 style=3D"width: 100%;">
                                                                <tr>
                                                                    <td ali=
gn=3D"right" valign=3D"middle">
                                                                        <p =
align=3D"right" class=3D"MsoNormal item_link" style=3D"color: #ff7100; font=
-size: 1em; font-weight: 500; line-height: 1em; margin: 0 15px 5px; padding=
: 0; text-align: right; text-decoration-color: transparent;">
                                                                           =
 <a href=3D"https://www.yad2.co.il/item/oqv49v63?topArea=3D2&rooms=3D3-5&pr=
ice=3D1000000-4000000&category=3Drealestate&subCategory=3Dforsale&isFromMyA=
lerts=3Dtrue&myAlertsSort=3D1&utm_source=3DmyAlertsRealestate&utm_medium=3D=
email&utm_campaign=3DmyAlertsAd" class=3D"MsoNormal item_link" target=3D"_b=
lank" style=3D"color: #ff7100; font-size: 1em; font-weight: 500; text-align=
: right; text-decoration-color: transparent;">
                                                                           =
     <span class=3D"MsoNormal item_link" style=3D"color: #ff7100; font-size=
: 1em; font-weight: 500; text-align: right; text-decoration-color: transpar=
ent;">=D7=9C=D7=A4=D7=A8=D7=98=D7=99=D7=9D =D7=A0=D7=95=D7=A1=D7=A4=D7=99=
=D7=9D</span>
                                                                           =
 </a>
                                                                        </p=
>
                                                                    </td>

                                                                    <td ali=
gn=3D"left" valign=3D"middle">
                                                                        <a =
class=3D"MsoNormal no_under_number" style=3D"color: #000000; font-size: 1em=
; font-weight: 400; pointer-events: none; text-decoration-color: transparen=
t;">
                                                                           =
 <p align=3D"left" class=3D"MsoNormal agency_name" style=3D"font-size: 0.75=
em; line-height: 1em; margin: 0 15px 5px; padding: 0; text-align: left;">
                                                                           =
     =D7=98=D7=99=D7=99=D7=A7=D7=95=D7=9F =D7=A0=D7=93=D7=9C"=D7=9F - =D7=
=AA=D7=95=D7=9E=D7=A8 =D7=A8=D7=95=D7=A1=D7=A7
                                                                           =
 </p>
                                                                        </a=
>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>

                                                    <tr><td height=3D"5"></=
td></tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td height=3D"10"></td>
                                        </tr>
                                    </table>
                               =20
                            </center>
                        </div>
                    </td>
                </tr>


                <!-- Feed Button -->
                <tr>
                    <td>
                        <style>
                            .feed_button_wrapper {
                                text-align: center;
                                font-size: 1em;
                                margin: 0;
                            }
                            .feed_button_link {
                                padding: 6px;
                                display: block;
                                text-decoration-color: transparent;
                            }
                            .feed_button_text {
                                color: #FFFFFF;
                                text-decoration-color: transparent;
                                text-align: center;
                                font-size: 1em;
                            }
                            .button_table {
                                max-width: 120px;=20
                            }
                            .button_wrapper {
                                text-align: center;
                            }
                        </style>
                       =20
                            <div align=3D"center" class=3D"feed_button_wrap=
per" style=3D"font-size: 1em; margin: 0; text-align: center;">
                                <center>
                                    <table class=3D"button_table" border=3D=
"0" cellpadding=3D"2" cellspacing=3D"3" bgcolor=3D"#FF7100" style=3D"max-wi=
dth: 120px;">
                                        <tr>
                                            <td class=3D"button_wrapper" st=
yle=3D"text-align: center;">
                                                <a href=3D"https://www.yad2=
.co.il/realestate/forsale?topArea=3D2&rooms=3D3-5&price=3D1000000-4000000&s=
tartDate=3D1656695436606-1656781836606&myAlertsSort=3D1&utm_source=3DmyAler=
tsRealestate&utm_medium=3Demail&utm_campaign=3DmyAlertsFeed" class=3D"MsoNo=
rmal feed_button_link" style=3D"display: block; padding: 6px; text-decorati=
on-color: transparent;">
                                                    <span class=3D"MsoNorma=
l feed_button_text" style=3D"color: #FFFFFF; font-size: 1em; text-align: ce=
nter; text-decoration-color: transparent;">=D7=9C=D7=9B=D7=9C =D7=94=D7=9E=
=D7=95=D7=93=D7=A2=D7=95=D7=AA</span>
                                                </a>
                                            </td>
                                        </tr>
                                    </table>
                                </center>
                            </div>
                       =20
                    </td>
                </tr>

                <!-- My Alerts Footer -->
                <tr>
                    <td>
                        <style>
    .y2-footer {
        background-color: #363636;
        text-align: center;
        width: 100%;
    }

    .highlighter-footer-text {
        color: #FFFFFF;
        text-decoration: underline;
    }

    .footer-per {
        margin: 0 0 15px;
        padding: 0;
        color: #999999;
        font-size: 0.75em;
    }

    .upper_per {
        margin-top: 10px;
    }

    .footer-section.upper p {
        margin-bottom: 20px;
    }
    .link_text {
        color: #FFFFFF;
        text-decoration-color: transparent;
        text-align: center;
        font-size: 1em;
    }
</style>

    <div align=3D"center" class=3D"MsoNormal">
        <center>
            <table bgcolor=3D"#363636" align=3D"center" class=3D"MsoNormal =
y2-footer" cellpadding=3D"5" cellspacing=3D"0" border=3D"0" style=3D"backgr=
ound-color: #363636; text-align: center; width: 100%;">
                <tr align=3D"center">
                    <td align=3D"center">
                        <p class=3D"MsoNormal footer-per upper_per" style=
=3D"color: #999999; font-size: 0.75em; margin: 0 0 15px; margin-top: 10px; =
padding: 0;">=D7=9C=D7=90 =D7=A8=D7=95=D7=A6=D7=94 =D7=9C=D7=A7=D7=91=D7=9C=
 =D7=94=D7=AA=D7=A8=D7=90=D7=95=D7=AA =D7=A2=D7=9C =D7=97=D7=99=D7=A4=D7=95=
=D7=A9 =D7=96=D7=94?=20
                            <a class=3D"MsoNormal highlighter-footer-text" =
href=3D"https://www.yad2.co.il/my-alerts?utm_source=3DmyAlertsRealestate&ut=
m_medium=3Demail&utm_campaign=3DmyAlertsRemoval" style=3D"color: #FFFFFF; t=
ext-decoration: underline;">=D7=9C=D7=94=D7=A1=D7=A8=D7=94</a>
                        </p>
                        <p class=3D"MsoNormal footer-per" style=3D"color: #=
999999; font-size: 0.75em; margin: 0 0 15px; padding: 0;">=D7=9C=D7=A9=D7=
=90=D7=9C=D7=95=D7=AA =D7=95=D7=91=D7=99=D7=A8=D7=95=D7=A8=D7=99=D7=9D =D7=
=A0=D7=95=D7=A1=D7=A4=D7=99=D7=9D =D7=A0=D7=99=D7=AA=D7=9F,=20
                            <a class=3D"MsoNormal highlighter-footer-text" =
href=3D"https://www.yad2.co.il/contactus" style=3D"color: #FFFFFF; text-dec=
oration: underline;">=D7=9C=D7=99=D7=A6=D7=95=D7=A8 =D7=90=D7=99=D7=AA=D7=
=A0=D7=95 =D7=A7=D7=A9=D7=A8 =D7=9B=D7=90=D7=9F</a>
                        </p>
                    </td>
                </tr>
                <tr class=3D"MsoNormal" align=3D"center">
                    <td align=3D"center" dir=3D"rtl">
                        <span>&nbsp;</span>
                        <a href=3D"https://www.yad2.co.il?utm_source=3DmyAl=
erts&utm_medium=3Demail&utm_campaign=3Dyad2" class=3D"MsoNormal link_text" =
target=3D"_blank" style=3D"color: #FFFFFF; font-size: 1em; text-align: cent=
er; text-decoration-color: transparent;">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/yad2.png" width=3D"35" height=
=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal CToWUd link_img" alt=
=3D"yad2">
                        </a>
                        <span>&nbsp;</span>
                        <a href=3D"https://www.yad2.co.il/contactus?utm_sou=
rce=3DmyAlerts&utm_medium=3Demail&utm_campaign=3Dcontact" class=3D"MsoNorma=
l link_text" target=3D"_blank" style=3D"color: #FFFFFF; font-size: 1em; tex=
t-align: center; text-decoration-color: transparent;">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/mail.png" width=3D"35" height=
=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal CToWUd link_img" alt=
=3D"mail">
                        </a>
                        <span>&nbsp;</span>
                        <a href=3D"https://www.facebook.com/yad2page" class=
=3D"MsoNormal link_text" target=3D"_blank" style=3D"color: #FFFFFF; font-si=
ze: 1em; text-align: center; text-decoration-color: transparent;">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/facebook.png" width=3D"35" heig=
ht=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal CToWUd link_img" alt=
=3D"facebook">
                        </a>
                        <span>&nbsp;</span>
                        <a href=3D"https://www.youtube.com/user/MeYad2" cla=
ss=3D"MsoNormal link_text" target=3D"_blank" style=3D"color: #FFFFFF; font-=
size: 1em; text-align: center; text-decoration-color: transparent;">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/youtube.png" width=3D"35" heigh=
t=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal CToWUd link_img" alt=
=3D"couture">
                        </a>
                        <span>&nbsp;</span>
                        <a href=3D"https://www.instagram.com/yad2page?igshi=
d=3Dtz8h99ziksyp" class=3D"MsoNormal link_text" target=3D"_blank" style=3D"=
color: #FFFFFF; font-size: 1em; text-align: center; text-decoration-color: =
transparent;">
                            <img src=3D"https://y2-notification-service.s3-=
eu-west-1.amazonaws.com/images/icons/footer/instagram.png" width=3D"35" hei=
ght=3D"35" hspace=3D"0" vspace=3D"0" class=3D"MsoNormal CToWUd link_img" al=
t=3D"instagram">
                        </a>
                    </td>
                </tr>
                <tr>=20
                    <td>
                        <hr>
                        <p class=3D"MsoNormal footer-per" style=3D"color: #=
999999; font-size: 0.75em; margin: 0 0 15px; padding: 0;">
                            =D7=A0=D7=99=D7=AA=D7=9F =D7=9C=D7=A4=D7=A0=D7=
=95=D7=AA =D7=90=D7=9C=D7=99=D7=A0=D7=95 =D7=91=D7=9E=D7=A1=D7=A4=D7=A8 <a =
class=3D"highlighter-footer-text" href=3D"tel:+972-3-5522222" style=3D"colo=
r: #FFFFFF; text-decoration: underline;">03-5522222</a>.=D7=91=D7=99=D7=9E=
=D7=99=D7=9D
                            =D7=90=D7=B3-=D7=94=D7=B3 =D7=91=D7=99=D7=9F =
=D7=94=D7=A9=D7=A2=D7=95=D7=AA 8:00-18:00,
                            <br>
                            =D7=91=D7=99=D7=9E=D7=99 =D7=95=D7=B3 =D7=95=D7=
=A2=D7=A8=D7=91=D7=99 =D7=97=D7=92 =D7=91=D7=99=D7=9F =D7=94=D7=A9=D7=A2=D7=
=95=D7=AA 8:00-13:00.
                        </p>
                    </td>=20
                </tr>
            </table>
        </center>
    </div>


                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
                                    </th>
                                </tr>
                            </table>
                        </center>
                    </td>
                </tr>
            </table>
        </div>
    </body>
</html>
"""
