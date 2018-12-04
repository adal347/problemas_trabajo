USE [CFDEmision33_Trans]
GO
/****** Object:  StoredProcedure [dbo].[InsCfdi33]    Script Date: 04/12/2018 09:25:26 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


-- =============================================
-- Autor:		Detecno
-- BD:
-- Rev: 		0
-- =============================================

ALTER  PROCEDURE [dbo].[InsCfdi33]
	@data	VARCHAR(MAX)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @xmlData						INT; -- ? Almacena el xml

	--PRINCIPAL
	DECLARE @facturaId						BIGINT;
	DECLARE @version						VARCHAR(3);--INT;
	DECLARE @serie							VARCHAR(50) = NULL;
	DECLARE @folio							VARCHAR(40);
	DECLARE @folio32						VARCHAR(40);
	DECLARE @estatusId						INT;
	DECLARE @estatusIdImpresion						INT;
	DECLARE @estatusIdCorreo					INT;
	DECLARE @estatusIdArchivo					INT;
	DECLARE @rechazoId						INT;
	DECLARE @fecha							VARCHAR(8);
	DECLARE @hora							VARCHAR(6);
	DECLARE @noCertificado					VARCHAR(20);
	DECLARE @certificado					NVARCHAR(MAX);
	DECLARE @formaPago					VARCHAR(4);
	DECLARE @condicionesDePago				VARCHAR(1000) = NULL;
	DECLARE @metodoPago					VARCHAR(4);
	DECLARE @tipoDeComprobante				VARCHAR(2);
	DECLARE @lugarExpedicion				VARCHAR(5);
	DECLARE @confirmacion					VARCHAR(4);

	--EMISOR
	DECLARE @rfc_Emisor						VARCHAR(13);
	DECLARE @nombre_Emisor					NVARCHAR(500);
	DECLARE @regimenFiscal					VARCHAR(3);
	DECLARE @calle_Emisor					NVARCHAR(500);
	DECLARE @noExterior_Emisor				NVARCHAR(50);
	DECLARE @noInterior_Emisor				NVARCHAR(50);
	DECLARE @colonia_Emisor					NVARCHAR(500);
	DECLARE @localidad_Emisor				NVARCHAR(500);
	DECLARE @referencia_Emisor				NVARCHAR(500);
	DECLARE @municipio_Emisor				NVARCHAR(250);
	DECLARE @estado_Emisor					NVARCHAR(250);
	DECLARE @pais_Emisor					NVARCHAR(250);
	DECLARE @codigoPostal_Emisor			NVARCHAR(5);

	--EXPEDIDO EN
	DECLARE @calle_EmisorEx					NVARCHAR(500);
	DECLARE @noExterior_EmisorEx			NVARCHAR(50);
	DECLARE @noInterior_EmisorEx			NVARCHAR(50);
	DECLARE @colonia_EmisorEx				NVARCHAR(500);
	DECLARE @localidad_EmisorEx				NVARCHAR(500);
	DECLARE @referencia_EmisorEx			NVARCHAR(500);
	DECLARE @municipio_EmisorEx				NVARCHAR(250);
	DECLARE @estado_EmisorEx				NVARCHAR(250);
	DECLARE @pais_EmisorEx					NVARCHAR(250);
	DECLARE @codigoPostal_EmisorEx			NVARCHAR(5);

	--RECEPTOR
	DECLARE @rfc_Receptor					VARCHAR(13);
	DECLARE @nombre_Receptor				VARCHAR(254);
	DECLARE @residenciaFiscal				VARCHAR(3);
	DECLARE @numRegIdTrib					VARCHAR(40);
	DECLARE @usoCfdi						VARCHAR(3);
	DECLARE @calle_Receptor					NVARCHAR(500);
	DECLARE @noExterior_Receptor			NVARCHAR(50);
	DECLARE @noInterior_Receptor			NVARCHAR(50);
	DECLARE @colonia_Receptor				NVARCHAR(500);
	DECLARE @localidad_Receptor				NVARCHAR(500);
	DECLARE @referencia_Receptor			NVARCHAR(500);
	DECLARE @municipio_Receptor				NVARCHAR(250);
	DECLARE @estado_Receptor				NVARCHAR(250);
	DECLARE @pais_Receptor					NVARCHAR(250);
	DECLARE @codigoPostal_Receptor			NVARCHAR(15);

	--TOTALES
	DECLARE @subTotal						NUMERIC(18,6);
	DECLARE @descuento						NUMERIC(18,6);
	DECLARE @moneda							VARCHAR(3);
	DECLARE @tipoCambio						NUMERIC(18,6);
	DECLARE @importeLetra					NVARCHAR(500);
	DECLARE @total							NUMERIC(18,6);
	DECLARE @totalImpuestosTrasladados		NUMERIC(18,6);
	DECLARE @totalImpuestosRetenidos		NUMERIC(18,6);

	--CONTROL
	DECLARE @cfdId							INT;
	DECLARE	@sucursal						NVARCHAR(500);
	DECLARE @addendaId						INT;
	DECLARE @pathImpresion					NVARCHAR(250);
	DECLARE	@correo							NVARCHAR(500);
	DECLARE @complementoId					INT;


	--CODIGO DE BARRAS
	DECLARE @valorCodigo					NVARCHAR(50);
	--FACTURA ORIGINAL
	DECLARE @folioFiscalO					NVARCHAR(36);
	DECLARE @serieFolio						NVARCHAR(25);
	DECLARE @fechaFolio						NVARCHAR(8);
	DECLARE @horaFolio						NVARCHAR(6);
	DECLARE @montoFolio						NUMERIC(20,6);
	--ADDENDAS
	DECLARE @spIns							nvarchar(50);
	DECLARE @executionLine					nvarchar(max);
	DECLARE @existeObjetoAddenda			int;
	DECLARE @fechaAddenda					NVARCHAR(25);

	--FOLIO
	DECLARE @automatico						NVARCHAR(20);
	--ADDENDA GENERAL
	DECLARE @nameS							NVARCHAR(max);
	DECLARE @schemaL						NVARCHAR(max);
	DECLARE @addendaGral					NVARCHAR(MAX);

	--COMPLEMENTOS
	DECLARE @spInsComplemento			    NVARCHAR(50);
	DECLARE @existeSpComplemento			INT;

	--INSERCION COMPLEMENTOS Y ADDENDAS
	DECLARE @error INT = NULL;
	DECLARE @errorNumber INT = NULL;
	DECLARE @errorMessage NVARCHAR(500) = NULL;
	DECLARE @errorSeverity INT = NULL;
	DECLARE @errorState nvarchar(500) = NULL;
	DECLARE @errorSp nvarchar(500) = NULL;
	DECLARE @errorLine INT = NULL;


	EXEC sp_xml_preparedocument @xmlData OUTPUT, @data; -- < Se genera la estructura del arbol XML;

	BEGIN
			BEGIN TRY
				BEGIN TRAN
					--Comprobante
					SELECT  @version=x.version, @serie=ISNULL(x.serie,''), @folio=ISNULL(x.folio,0),  @fecha=REPLACE(SUBSTRING(x.fecha,0,CHARINDEX('T',x.fecha,0)),'-',''), @hora=REPLACE(SUBSTRING(x.fecha,CHARINDEX('T',x.fecha,0)+1,LEN(x.fecha)-LEN(CHARINDEX('T',x.fecha,0))),':',''), @formaPago=x.formaPago, @condicionesDePago=x.condicionesDePago, @tipoDeComprobante=x.tipoDeComprobante, @metodoPago=x.metodoPago ,@lugarExpedicion = x.lugarExpedicion,@confirmacion = x.confirmacion
					FROM OPENXML(@xmlData,'/Comprobante',1)
					WITH ( version VARCHAR(3),serie VARCHAR(50), folio VARCHAR(40), fecha VARCHAR(25), formaPago VARCHAR(4), tipoDeComprobante VARCHAR(2), condicionesDePago VARCHAR(1000), metodoPago VARCHAR(4), lugarExpedicion VARCHAR(5),  confirmacion VARCHAR(5)) AS x;
					--Emisor
					SELECT @rfc_Emisor=x.rfc, @nombre_Emisor=x.nombre, @regimenFiscal=x.regimenFiscal
					FROM OPENXML(@xmlData,'/Comprobante/Emisor',1)
					WITH (rfc VARCHAR(13), nombre VARCHAR(500), regimenFiscal VARCHAR(3)) AS x;
					--Domicilio Fiscal
					SELECT @calle_Emisor=x.calle, @noExterior_Emisor=x.noExterior, @noInterior_Emisor=x.noInterior, @colonia_Emisor=x.colonia, @localidad_Emisor=x.localidad, @referencia_Emisor=x.referencia, @municipio_Emisor=x.municipio, @estado_Emisor=x.estado, @pais_Emisor=x.pais, @codigoPostal_Emisor=x.codigoPostal
					FROM OPENXML(@xmlData,'/Comprobante/Emisor/DomicilioFiscal',1)
					WITH (calle NVARCHAR(500), noExterior NVARCHAR(50), noInterior NVARCHAR(50), colonia NVARCHAR(500), localidad NVARCHAR(500), referencia NVARCHAR(500), municipio NVARCHAR(250), estado NVARCHAR(250), pais NVARCHAR(250), codigoPostal NVARCHAR(5)) AS x;
					--Expedido En
					SELECT @calle_EmisorEx=x.calle, @noExterior_EmisorEx=x.noExterior, @noInterior_EmisorEx=x.noInterior, @colonia_EmisorEx=x.colonia, @localidad_EmisorEx=x.localidad, @referencia_EmisorEx=x.referencia, @municipio_EmisorEx=x.municipio, @estado_EmisorEx=x.estado, @pais_EmisorEx=x.pais, @codigoPostal_EmisorEx=x.codigoPostal
					FROM OPENXML (@xmlData,'/Comprobante/Emisor/ExpedidoEn',1)
					WITH (calle NVARCHAR(500), noExterior NVARCHAR(50), noInterior NVARCHAR(50), colonia NVARCHAR(500), localidad NVARCHAR(500), referencia NVARCHAR(500), municipio NVARCHAR(250), estado NVARCHAR(250), pais NVARCHAR(250), codigoPostal NVARCHAR(5)) AS x;
					--Receptor
					SELECT @rfc_Receptor=x.rfc, @nombre_Receptor=x.nombre, @residenciaFiscal = x.residenciaFiscal, @numRegIdTrib = x.numRegIdTrib,@usoCfdi = x.usoCfdi
					FROM OPENXML(@xmlData,'/Comprobante/Receptor',1)
					WITH (rfc NVARCHAR(13), nombre NVARCHAR(254), residenciaFiscal VARCHAR(3), numRegIdTrib VARCHAR(40), usoCfdi VARCHAR(3)) AS x;
					--Domicilio
					SELECT @calle_Receptor=x.calle, @noExterior_Receptor=x.noExterior, @noInterior_Receptor=x.noInterior, @colonia_Receptor=x.colonia, @localidad_Receptor=x.localidad, @referencia_Receptor=x.referencia, @municipio_Receptor=x.municipio, @estado_Receptor=x.estado, @pais_Receptor=x.pais, @codigoPostal_Receptor=x.codigoPostal
					FROM OPENXML(@xmlData,'/Comprobante/Receptor/Domicilio',1)
					WITH (calle VARCHAR(500), noExterior NVARCHAR(50), noInterior NVARCHAR(50), colonia NVARCHAR(500), localidad NVARCHAR(500), referencia NVARCHAR(500), municipio NVARCHAR(250), estado NVARCHAR(250), pais NVARCHAR(250), codigoPostal NVARCHAR(50)) AS x;
					--Control
					SELECT @cfdId=x.cfdid,	@sucursal=x.sucursal,   @estatusId=x.estatusId,@estatusIdImpresion = estatusIdImpresion , @estatusIdCorreo= estatusIdCorreo, @estatusIdArchivo=x.estatusIdArchivo, @rechazoId=x.rechazoId, @addendaId=x.addendaId,   @pathImpresion=x.pathImpresion,@correo=x.correo , @complementoId =  x.complementoId
					FROM OPENXML(@xmlData,'/Comprobante/Control',1)
					WITH (cfdid INT, sucursal NVARCHAR(500), estatusId INT, estatusIdImpresion INT, estatusIdCorreo INT,  estatusIdArchivo INT, rechazoId INT, addendaId INT, pathImpresion NVARCHAR(250), correo NVARCHAR(500), formatoImpresion NVARCHAR(50), formatoCorreo INT, formatoWeb INT, complementoId INT) AS x;
					-- CONTROL DE FOLIOS
					SELECT @automatico=x.automatico
					FROM OPENXML(@xmlData, '/Comprobante/Foliado',1)
					WITH (automatico nvarchar(20)) as x
					IF @automatico='true'
					BEGIN
						--SET @folio=(SELECT ISNULL(MAX([001FOLIO]),0)
						--FROM CFDEmision33_cons.DBO.T001_PRINCIPAL WITH(NOLOCK)
						--INNER JOIN CFDEmision33_cons.DBO.T002_Emisor WITH(NOLOCK) ON [001facturaid] = [002facturaid]
						--WHERE [002rfc]=(@rfc_Emisor)
						--AND [001SERIE] =(@serie));

						SELECT  @folio=ISNULL(MAX([001FOLIO]), 0) FROM CFDEmision33_cons.DBO.Folios33
						WHERE [002RFC]=@rfc_Emisor AND [001SERIE]=@serie

						set @folio = @folio + 1



						IF @folio = '1'
						BEGIN
							SET @folio32=(SELECT ISNULL(MAX(Folio),0)+1
							FROM CFDEmision33_cons.DBO.Folios32_prox WITH(NOLOCK)
							WHERE RFC_Emisor=(@rfc_Emisor)
							AND Serie =(@serie));

							SET @folio = @folio32;
						END

					END
				COMMIT

				--T001_PRINCIPAL
				BEGIN TRAN
					INSERT INTO [dbo].[T001_Principal]([001version],[001serie],[001folio],[001estatusId],[001estatusIdImpresion],[001estatusIdCorreo],[001estatusIdArchivo],[001rechazoId],[001fecha],[001hora],[001noCertificado],[001certificado],[001formaPago],[001condicionesDePago],[001metodoPago],[001tipoDeComprobante],[001lugarExpedicion],[001confirmacion])
					VALUES (@version,@serie,@folio,0,@estatusIdImpresion,@estatusIdCorreo,@estatusIdArchivo,@rechazoId,@fecha,@hora,@noCertificado,@certificado,@formaPago,@condicionesDePago,@metodoPago,@tipoDeComprobante,@lugarExpedicion,@confirmacion);
					SELECT @facturaId = SCOPE_IDENTITY();
				COMMIT

				BEGIN TRAN
					IF NOT EXISTS(SELECT 1 FROM CFDEmision33_cons.DBO.Folios33
						WHERE [002RFC]=@rfc_Emisor AND [001SERIE]=@serie)
					BEGIN
						INSERT INTO CFDEmision33_cons.DBO.Folios33 ( [002RFC],  [001SERIE], [001Folio])
						VALUES (@rfc_Emisor, @serie, @folio)
					END
					ELSE
					BEGIN
						UPDATE CFDEmision33_cons.DBO.Folios33
						SET  [001Folio]=@folio
						WHERE [002RFC]=@rfc_Emisor AND [001SERIE]=@serie
					END
					--T002_Emisor
					INSERT INTO T002_Emisor ([002facturaId],[002tipo],[002rfc],[002nombre],[002regimenFiscal],[002calle],[002noExterior],[002noInterior],[002colonia],[002localidad],[002referencia],[002municipio],[002estado],[002pais],[002cp])
					VALUES (@facturaId,'0',@rfc_Emisor,@nombre_Emisor,@regimenFiscal,@calle_Emisor,@noExterior_Emisor,@noInterior_Emisor,@colonia_Emisor,@localidad_Emisor,@referencia_Emisor,@municipio_Emisor,@estado_Emisor,@pais_Emisor,@codigoPostal_Emisor);

					INSERT INTO T002_Emisor ([002facturaId],[002tipo],[002rfc],[002nombre],[002regimenFiscal],[002calle],[002noExterior],[002noInterior],[002colonia],[002localidad],[002referencia],[002municipio],[002estado],[002pais],[002cp])
					VALUES (@facturaId,'1',@rfc_Emisor,@nombre_Emisor,@regimenFiscal,@calle_EmisorEx,@noExterior_EmisorEx,@noInterior_EmisorEx,@colonia_EmisorEx,@localidad_EmisorEx,@referencia_EmisorEx,@municipio_EmisorEx,@estado_EmisorEx,@pais_EmisorEx,@codigoPostal_EmisorEx);

					--T003_Receptor
					INSERT INTO T003_Receptor ([003facturaId],[003rfc],[003nombre],[003residenciaFiscal],[003numRegIdTrib],[003usoCfdi],[003calle],[003noExterior],[003noInterior],[003colonia],[003localidad],[003referencia],[003municipio],[003estado],[003pais],[003cp])
					VALUES (@facturaId,@rfc_Receptor,@nombre_Receptor,@residenciaFiscal,@numRegIdTrib,@usoCfdi,@calle_Receptor,@noExterior_Receptor,@noInterior_Receptor,@colonia_Receptor,@localidad_Receptor,@referencia_Receptor,@municipio_Receptor,@estado_Receptor,@pais_Receptor,@codigoPostal_Receptor);

					--T004_Detalle
					INSERT INTO T004_Detalle([004facturaId],[004ordenador],[004idPadre],[004nivel],[004claveProdServ],[004cantidad],[004claveUnidad],[004unidad],[004noIdentificacion],[004descripcion],[004valorUnitario],[004importe],[004descuento],[004extra1],[004extra2],[004extra3],[004extra4],[004extra5],[004extra6],[004extra7],[004extra8],[004extra9],[004extra10],[004extra11],[004extra12],[004extra13],[004extra14],[004extra15],[004extra16],[004extra17],[004extra18],[004extra19],[004extra20],[004impuesto],[004numTransaccion],[004impTraslados],[004impRetenidos],[004fechaEfectiva],[term],[004nivelConcepto])
					SELECT @facturaId, x.ordenador, x.padre, x.nivel, x.claveProdServ ,x.cantidad, x.claveUnidad, x.unidad, x.noIdentificacion, x.descripcion, x.valorUnitario, x.importe, x.descuento, x.extra1, x.extra2, x.extra3, x.extra4, x.extra5, x.extra6, x.extra7, x.extra8, x.extra9, x.extra10, x.extra11, x.extra12, x.extra13, x.extra14, x.extra15, x.extra16, x.extra17, x.extra18, x.extra19, x.extra20, x.impuesto, x.transaccion, x.Traslado, x.Retenido, x.fechaEfectiva, x.term, x.nivelConcepto
					FROM OPENXML(@xmlData,'/Comprobante/Conceptos/Concepto',1)
					WITH (ordenador INT, padre INT, nivel INT, claveProdServ VARCHAR(10), cantidad varchar(30), claveUnidad VARCHAR(4), unidad NVARCHAR(50), noIdentificacion NVARCHAR(50), descripcion NVARCHAR(1000), valorUnitario varchar(30), importe varchar(30), descuento NUMERIC(18,2), extra1 NVARCHAR(1000), extra2 NVARCHAR(1000), extra3 NVARCHAR(1000), extra4 NVARCHAR(1000), extra5 NVARCHAR(1000), extra6 NVARCHAR(1000), extra7 NVARCHAR(1000), extra8 NVARCHAR(1000), extra9 NVARCHAR(1000), extra10 NVARCHAR(1000), extra11 NVARCHAR(1000), extra12 NVARCHAR(1000), extra13 NVARCHAR(1000), extra14 NVARCHAR(1000), extra15 NVARCHAR(1000), extra16 NVARCHAR(1000), extra17 NVARCHAR(1000), extra18 NVARCHAR(1000), extra19 NVARCHAR(1000), extra20 NVARCHAR(1000), impuesto NVARCHAR(1000), transaccion NVARCHAR(50), Traslado NVARCHAR(1000), Retenido NVARCHAR(1000), fechaEfectiva varchar(10), term varchar(7), nivelConcepto varchar(20)) AS x;

					--T005_ImpuestosConcepto
					INSERT INTO [dbo].[T005_ImpuestosConcepto]
					SELECT d.[004detalleId] as detalleId, x.base, x.impuesto, x.tipoFactor, x.tasaOCuota, x.importe,'T' AS 'tipo'
					FROM OPENXML (@xmlData,'/Comprobante/Conceptos/Concepto/Impuestos/Traslados/Traslado',1)
					WITH (detalleId bigint, base VARCHAR(30), impuesto VARCHAR(3), tipoFactor VARCHAR(10), tasaOCuota NUMERIC(18,6), importe VARCHAR(30) , ordenador INT) AS x
					LEFT JOIN T004_Detalle AS d with(nolock) ON x.ordenador=d.[004ordenador]
					WHERE d.[004facturaId] = @facturaId and d.[004ordenador] = x.ordenador;

					--T005_ImpuestosConcepto
					INSERT INTO [dbo].[T005_ImpuestosConcepto]
					SELECT d.[004detalleId] as detalleId, x.base, x.impuesto, x.tipoFactor, x.tasaOCuota, x.importe,'R' AS 'tipo'
					FROM OPENXML (@xmlData,'/Comprobante/Conceptos/Concepto/Impuestos/Retenciones/Retencion',1)
					WITH (detalleId bigint, base DECIMAL(18,6), impuesto VARCHAR(3), tipoFactor VARCHAR(10), tasaOCuota NUMERIC(18,6), importe NUMERIC(18,6) , ordenador INT) AS x
					LEFT JOIN T004_Detalle AS d with(nolock) ON x.ordenador=d.[004ordenador]
					WHERE d.[004facturaId] = @facturaId and d.[004ordenador] = x.ordenador;

					--T006_Aduana
					INSERT INTO [dbo].[T006_Aduana]
					SELECT d.[004detalleId] as detalleId, x.numeroPedimento
					FROM OPENXML (@xmlData,'/Comprobante/Conceptos/Concepto/InformacionAduanera',1)
					WITH (detalleId bigint, numeroPedimento NVARCHAR(21), ordenador INT) AS x
					LEFT JOIN T004_Detalle AS d with(nolock) ON x.ordenador=d.[004ordenador]
					WHERE d.[004facturaId] = @facturaId and d.[004ordenador] = x.ordenador;

					----T007_Total
					INSERT INTO [dbo].[T007_Total]
					SELECT @facturaid,  x.subTotal, x.descuento, x.moneda, x.tipoCambio,  x.importeLetra, x.total, x.totalImpuestosRetenidos, x.totalImpuestosTrasladados
					FROM OPENXML(@xmlData,'/Comprobante/Totales',1)
					WITH (subTotal NUMERIC(18,6), descuento NUMERIC(18, 6), moneda VARCHAR(3),tipoCambio NUMERIC(18, 6),  total NUMERIC(18,6),importeLetra NVARCHAR(500),  totalImpuestosRetenidos NUMERIC(18,6), totalImpuestosTrasladados NUMERIC(18,6)) as x;

					----T008_Impuesto
					INSERT INTO [dbo].[T008_Impuesto]
					SELECT @facturaid, x.ordenador,x.impuesto,'', x.tasaOCuota, x.importe, 'R' AS 'tipo',I.[206impCat]
					FROM OPENXML(@xmlData,'/Comprobante/Impuestos/Retenciones/Retencion')
					WITH (ordenador INT, impuesto VARCHAR(3),importe NUMERIC(18,2), tasaOCuota NVARCHAR(10)) AS x
					INNER JOIN [dbo].[T206_Impuestos] AS I WITH(NOLOCK) ON  x.ordenador=I.[206impuestoId];

					----T008_Impuesto
					INSERT INTO [dbo].[T008_Impuesto]
					SELECT @facturaid, x.ordenador,x.impuesto,x.tipoFactor,x.tasaOCuota,x.importe, 'T' AS 'tipo', I.[206impCat]
					FROM OPENXML(@xmlData,'/Comprobante/Impuestos/Traslados/Traslado')
					WITH (ordenador INT, impuesto VARCHAR(3), tipoFactor VARCHAR(10),importe NUMERIC(18,2), tasaOCuota NVARCHAR(10)) AS x
					INNER JOIN [dbo].[T206_Impuestos] AS I WITH(NOLOCK) ON  x.ordenador=I.[206impuestoId] ;

					----T010_Control
					INSERT INTO [dbo].[T010_Control]([010facturaId],[010cfdId],[010sucursal],[010addendaId],[010pathImpresion],[010correo],[010formatoImpresion],[010formatoCorreo],[010formatoWeb],[010complementoId])
					SELECT @facturaid, x.cfdId, x.sucursal,x.addendaId, x.pathImpresion, x.correo, x.formatoImpresion, x.formatoCorreo, x.formatoWeb, x.complementoId
					FROM OPENXML(@xmlData,'/Comprobante/Control',1)
					WITH (cfdId INT, sucursal NVARCHAR(500), addendaId INT, pathImpresion NVARCHAR(250), correo NVARCHAR(500), formatoImpresion NVARCHAR(50), formatoCorreo INT, formatoWeb INT, complementoId INT) as x;

					----T011_Comentario
					INSERT INTO [dbo].[T011_Comentario]([011facturaId], [011descripcion])
					SELECT @facturaid, x.descripcion
					FROM OPENXML(@xmlData,'/Comprobante/Comentarios',1)
					WITH (descripcion NVARCHAR(MAX)) as x;

					----T012_Extra
					INSERT INTO [dbo].[T012_Extra]
					SELECT @facturaid, x.extra1, x.extra2, x.extra3, x.extra4, x.extra5, x.extra6, x.extra7, x.extra8, x.extra9, x.extra10, x.extra11, x.extra12, x.extra13, x.extra14, x.extra15, x.extra16, x.extra17, x.extra18, x.extra19, x.extra20, x.extra21, x.extra22, x.extra23, x.extra24, x.extra25, x.extra26, x.extra27, x.extra28, x.extra29, x.extra30, x.extra31, x.extra32, x.extra33, x.extra34, x.extra35, x.extra36, x.extra37, x.extra38, x.extra39, x.extra40, x.extra41, x.extra42, x.extra43, x.extra44, x.extra45, x.extra46, x.extra47, x.extra48, x.extra49, x.extra50
					FROM OPENXML(@xmlData,'/Comprobante/DatosExtraCFD',1)
					WITH (extra1 NVARCHAR(MAX), extra2 NVARCHAR(MAX), extra3 NVARCHAR(MAX), extra4 NVARCHAR(MAX), extra5 NVARCHAR(MAX), extra6 NVARCHAR(MAX), extra7 NVARCHAR(MAX), extra8 NVARCHAR(MAX), extra9 NVARCHAR(MAX), extra10 NVARCHAR(MAX), extra11 NVARCHAR(MAX), extra12 NVARCHAR(MAX), extra13 NVARCHAR(MAX), extra14 NVARCHAR(MAX), extra15 NVARCHAR(MAX), extra16 NVARCHAR(MAX), extra17 NVARCHAR(MAX), extra18 NVARCHAR(MAX), extra19 NVARCHAR(MAX), extra20 NVARCHAR(MAX), extra21 NVARCHAR(MAX), extra22 NVARCHAR(MAX), extra23 NVARCHAR(MAX), extra24 NVARCHAR(MAX), extra25 NVARCHAR(MAX), extra26 NVARCHAR(MAX), extra27 NVARCHAR(MAX), extra28 NVARCHAR(MAX), extra29 NVARCHAR(MAX), extra30 NVARCHAR(MAX), extra31 NVARCHAR(MAX), extra32 NVARCHAR(MAX), extra33 NVARCHAR(MAX), extra34 NVARCHAR(MAX), extra35 NVARCHAR(MAX), extra36 NVARCHAR(MAX), extra37 NVARCHAR(MAX), extra38 NVARCHAR(MAX), extra39 NVARCHAR(MAX), extra40 NVARCHAR(MAX), extra41 NVARCHAR(MAX), extra42 NVARCHAR(MAX), extra43 NVARCHAR(MAX), extra44 NVARCHAR(MAX), extra45 NVARCHAR(MAX), extra46 NVARCHAR(MAX), extra47 NVARCHAR(MAX), extra48 NVARCHAR(MAX), extra49 NVARCHAR(MAX), extra50 NVARCHAR(MAX)) as x;

					----T013_CodigoBarras  varios codigos
					INSERT INTO T013_CodigoBarras([013facturaId],[013valor], [013tipoId], [013ordenador])
					SELECT @facturaid, x.valorCodigo, x.tipoCodigo ,x.ordenador
					FROM OPENXML(@xmlData,'/Comprobante/CodigoBarras/CodBar',1)
					WITH (valorCodigo NVARCHAR(50), tipoCodigo INT,ordenador INT) as x;

					----[dbo].[T017_CfdiRelacionados]
					INSERT INTO [dbo].[T017_CfdiRelacionados]
					SELECT @facturaid, x.tipoRelacion, null, '0' as tipo, null
					FROM OPENXML(@xmlData,'/Comprobante/CfdiRelacionados',1)
					WITH (tipoRelacion VARCHAR(3)) as x;

					INSERT INTO [dbo].[T017_CfdiRelacionados]
					SELECT @facturaid, null, x.UUID, '1' as tipo, x.ordenador
					FROM OPENXML(@xmlData,'/Comprobante/CfdiRelacionados/CfdiRelacionado',1)
					WITH ( UUID VARCHAR(36), ordenador INT) as x;

					--------------------------------------------------------------------------------------------------------------------
					/************************************************COMPLEMENTOS******************************************************/
					--------------------------------------------------------------------------------------------------------------------
					--Validar si tiene complemento id para su insercion.
					DECLARE @TablaErrorIns TABLE (error INT,ErrorNumber INT, ErrorMessage NVARCHAR(500),ErrorSeverity INT,ErrorState NVARCHAR(500), ErrorSP NVARCHAR(500), ErrorLine INT)

					SELECT  @complementoId = x.complementoId
					FROM OPENXML(@xmlData,'/Comprobante/Control',1)
					WITH (complementoId INT) AS x;

					IF (@complementoId is not null and @complementoId > 0)
						BEGIN
							SET @spInsComplemento = (SELECT [215spIns] FROM T215_Complementos WHERE [215complementoId] = @complementoId)
							SET @existeSpComplemento =(SELECT count(0) FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = @spInsComplemento)
																insert into [xmlPretimbrado] values (@data,@complementoId,@executionLine,@existeSpComplemento);
							IF @existeSpComplemento > 0
								BEGIN
									SET @executionLine = 'Exec ' + @spInsComplemento + ' ' + Convert(nvarchar,@facturaId) + ' ,' + char(39) + @data + char(39)
									INSERT INTO @TablaErrorIns  EXEC (@executionLine)
									SELECT  @error = Error,@errorNumber = ErrorNumber,@errorMessage = ErrorMessage, @errorSeverity  = ErrorSeverity , @errorState  = ErrorState, @errorSp  = ErrorSp, @errorLine  = ErrorLine  from @TablaErrorIns
								END
						END
					--EVALUAMOS SI EXISTE ERROR EN LA INSERCION DEL COMPLEMENTO
					IF (@error > 0)
						 BEGIN
							ROLLBACK  TRANSACTION;
							RAISERROR(@errorMessage,@errorSeverity,@errorState);
						 END

					--------------------------------------------------------------------------------------------------------------------
					/************************************************ADDENDAS**********************************************************/
					--------------------------------------------------------------------------------------------------------------------

					--T401_Cliente - Validar que la AddendaID sea 1 y proceder a la Insercion
					SELECT  @addendaId = x.addendaId
					FROM OPENXML(@xmlData,'/Comprobante/Control',1)
					WITH (addendaId INT) AS x;

					IF (@addendaId is not null and @addendaId > 1)
						BEGIN
							SET @spIns = (SELECT [205spIns] FROM T205_Addenda WHERE [205addendaId] = @addendaId)
							SET @existeObjetoAddenda =(SELECT count(0) FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = @spIns)
							IF @existeObjetoAddenda > 0
								BEGIN
									SET @executionLine = 'Exec ' + @spIns + ' ' + Convert(nvarchar,@facturaId) + ' ,' + char(39) + @data + char(39)
									INSERT INTO @TablaErrorIns  EXEC (@executionLine)
									SELECT  @error = Error,@errorNumber = ErrorNumber,@errorMessage = ErrorMessage, @errorSeverity  = ErrorSeverity , @errorState  = ErrorState, @errorSp  = ErrorSp, @errorLine  = ErrorLine  from @TablaErrorIns
								END
						END
						--EVALUAMOS SI EXISTE ERROR EN LA INSERCION DE LA ADDENDA
					IF (@error > 0)
						 BEGIN
							ROLLBACK  TRANSACTION;
							RAISERROR(@errorMessage,@errorSeverity,@errorState);
						 END

					IF (@addendaId=1)
						BEGIN
						declare @xmlAddGral xml;

						SELECT  @xmlAddGral = x.AddendaGral
						FROM   OPENXML (@xmlData, '/Comprobante/Addenda/AddendaGeneral/*', 10)
						WITH   ( AddendaGral xml '@mp:xmltext' )  as x;


						set @addendaGral = (select CONVERT(nvarchar(max), @xmlAddGral));
						SELECT  @nameS=xx.nameS,@schemaL =xx.schemaL
						FROM OPENXML(@xmlData,'/Comprobante/Addenda',2)
						WITH (nameS            NVARCHAR(MAX),schemaL		 NVARCHAR(MAX)) as xx;

						INSERT INTO T401_Cliente([401facturaId], [401descripcion],[401nombre], [401ns], [401sl])
						SELECT @facturaid, @addendaGral, x.addendaNombre,@nameS, @schemaL
						FROM OPENXML(@xmlData,'/Comprobante/Addenda/AddendaGeneral',1)
						WITH (addendaNombre NVARCHAR(MAX))  as x;

					END

					UPDATE T001_PRINCIPAL SET [001ESTATUSID] = 1 WHERE [001FACTURAID] = @facturaid
					SELECT '0' AS Error, '0' AS errorNumber, '' AS errorMessage, '' AS errorSeverity , '' AS errorState, '' AS errorLine, '' AS errorProcedure ,@facturaId AS 'FacturaId';
				COMMIT TRANSACTION;
			END TRY
			BEGIN CATCH

				IF (@error > 0)
				BEGIN
					SELECT '1' AS Error, @errorNumber AS errorNumber, @errorMessage AS errorMessage, @errorSeverity AS errorSeverity , @errorState AS errorState,@errorLine AS errorLine, @errorSp AS errorProcedure , '' AS 'FacturaId';
				END
				ELSE
				BEGIN
					ROLLBACK  TRANSACTION;
					SELECT '1' AS Error, ERROR_NUMBER() AS errorNumber, ERROR_MESSAGE() AS errorMessage, ERROR_SEVERITY() AS errorSeverity , ERROR_STATE() AS errorState, error_line() AS errorLine, ERROR_PROCEDURE() AS errorProcedure ,@facturaId AS 'FacturaId';
				END
				IF(@facturaId IS NOT NULL)
				BEGIN
					DELETE T001_Principal WHERE [001facturaId]=@facturaId;
				END
			END CATCH
	END

	EXEC sp_xml_removedocument @xmlData; -- < Se destruye la estructura del arbol XML
END
